Billing documentation
=====================

Transactions
------------

### Idempotence identifier

Image a situation when client tries to transfer money using your REST API.
The frontend sends POST request to transfer money, the server successfully processes the request,
but something happens with the network during REST API response receiving.

The client see "an error" and tries to repeat the same transfer operation.
But the previous one already successfully finished! So the client spends his money twice!

To prevent that case we change the flow:
* Client ask a new transaction_id
* Client calls transfer money endpoint with given transaction_id
* Sever creates all payments (& change client balance, or place it in queue)
* Network issues happens during server response reading
* Client tries to do the same operation with the same transaction_id
* Server see that that transaction_id already processed and returns 409 response
* Client understand that previous operation was successfully done & just retrieve
  information about current status by transaction_id

A bit about transaction_id: it should be unique for all instances.

### Transaction payments

The transaction connects 2 (or more, in general) sides:
* Money transfer: it connects 2 clients.
* Balance recharge: it connects billing with client
  (billing sends money to client).
* Money withdraw: it connects client & billing
  (client sends money to billing's "withdraw wallet".)

As we want to scale our database, we have a payment record per each side,
so we can split our database by client_id ranges, putting clients from
the same transaction in different shards.

The transaction is done when all its payments done.

If one or more payments were canceled we have to cancel the whole transaction.

Once transaction accepted / done, wallets balances changed.

If you wanna correct client's balance, please make additional
"correction" transaction.

See also: [wallets](wallets.md "wallets"), [payments](payments.md "payments").

### Transactions table

**tbl_transactions**

| field                    | type     | comment                                            |
|:-------------------------|:--------:|:---------------------------------------------------|
| id                       | uuid     |                                                    |
| created_at               | datetime |                                                    |
| updated_at               | datetime |                                                    |
| transaction_type         | int      | transfer, recharge, withdraw, correction           |
| transaction_status       | int      | created, rejected, accepted, done                  |

We don't really need that table in this task, actually, because we already store that data in payments table.
If you wanna make horizontal sharding it's also not so useful, because transactions table is one of the biggest table.
