Please, follow the task and try not to make anything extra. PEP8 is required. It is expected a
small description of chosen technologies and architecture in the README file. It is
supposed that a solution will be used with big data volume. The solution should launch easily for check (for example, using Docker).
The choice of frameworks and libraries up to you. Python 3.6+ using is desirable.

It is required to implement a simple payment system Web application
Base currency of the service — USD.
Available wallet currencies - USD, EUR, CAD, CNY

Requirements:

1. Each client of service has one «wallet» with money in some
currency

2. There is a possibility to get information about client name,
country, city, wallet currency and current balance.

3. Clients can make transfers between each other with any currency
available in the system.

4. All operations are stored in the system. As an advantage, if
operations will have a status model with statuses history.

5. There is the method to get information about currency rates to USD
at the time of operation creation from an external source (can be mocked).

6. The solution is a REST API project, with main operations for
wallets, and also for reports.

7. Required endpoints for REST API:
   * client registration with their name, country, city and currency of wallet
   * wallet top-up
   * transfer between wallets
   * information about users' balance
   * report (see below)

8. Report should contain wallet history with operations and balance
after each of operation. Possible fields: date, from, to, amount, balance
Report parameters: wallet (required), start_date (not required),
end_date (not required).
In addition, there is a possibility to export report into CSV and
XML.

9. Tests. 100% coverage is not required
