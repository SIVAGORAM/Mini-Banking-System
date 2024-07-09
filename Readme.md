Developed an ATM Simulation System in Python, implementing user authentication, balance management, and transaction processing for withdrawals and deposits. Utilized object-oriented programming principles to design secure and user-friendly functionalities. Ensured robust input validation and error handling throughout the application. Demonstrated proficiency in creating real-world system simulations through software development.

ATM System in Python
Objective:
To develop an ATM system in Python that allows users to perform banking transactions such as balance inquiries, deposits, withdrawals, mini statements, and PIN changes with enhanced security features.

Key Features:
PIN Verification and Security:

Users enter a PIN to access their account.
The system verifies the entered PIN against a predefined list of valid PINs.
If the PIN is incorrect, the number of attempts is tracked.
After three incorrect attempts, the account is locked for a specified duration (1 minute).
Balance Inquiry:

Users can view their current account balance.
Deposits:

Users can deposit money into their account.
Deposits update the account balance and are recorded in the transaction history.
Withdrawals:

Users can withdraw money from their account, provided they have sufficient funds.
Withdrawals update the account balance and are recorded in the transaction history.
Mini Statement:

Users can view the last five transactions (deposits and withdrawals) performed on their account.
PIN Change:

Users can change their current PIN to a new one, ensuring it is unique and not already in use.
Detailed Functionality:
CheckPin Class:

Manages the verification of PINs.
Tracks incorrect attempts and locks accounts after three incorrect attempts.
Allows updating of PINs.
Balance Class:

Manages the account balance and transaction history.
Provides methods to get the current balance and update it with deposits and withdrawals.
Transaction Class:

Abstract class for handling transactions.
Subclasses: Withdraw and Deposit handle specific transaction types and update the balance accordingly.
ATM Class:

Manages the user interface and interactions.
Prompts users for their PIN and handles the main menu for transactions.
Executes user choices for withdrawing, depositing, viewing mini statements, and changing PINs.
Example Workflow:
User enters their PIN.
If the PIN is correct, the user is prompted with a menu:
Withdraw: The user enters an amount and, if sufficient funds are available, the amount is withdrawn.
Deposit: The user enters an amount, which is added to the account balance.
Mini Statement: The last five transactions are displayed.
Change PIN: The user can change their PIN to a new one.
If the PIN is incorrect, the attempt is recorded. After three incorrect attempts, the account is locked for 1 minute.
Benefits:
Provides a secure and straightforward interface for ATM transactions.
Ensures user accounts are protected against unauthorized access with PIN verification and account lock features.
Maintains a history of recent transactions for user reference.
Future Enhancements:
Integrate with a real bank database for dynamic account management.
Implement a graphical user interface (GUI) for a more user-friendly experience.
Add support for additional transaction types and features such as fund transfers and bill payments.
