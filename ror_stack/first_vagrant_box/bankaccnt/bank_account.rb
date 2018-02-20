class BankAccount
  attr_reader :account_number, :checking_balance, :savings_balance, :total_number_of_accounts

  @@total_number_of_accounts = 0



  # ------------ Initialize Stuff
  def initialize interestRate = 0.1
    @account_number = account_number
    @checking_balance = 0.0
    @savings_balance = 0.0

    @interestRate = interestRate

    @@total_number_of_accounts += 1
  end



  def generate_account_number
    account_number = ""
    8.times do
      account_number << rand(0...8).to_s
    end
    return account_number
  end



  def can_instance_read_class_variable?
    puts @@total_number_of_accounts
  end



  # ------------ Account Functionality
  def account_info
    puts "the interest rate for account #{@account_number} is: #{@interestRate}"
    account_balances
  end



  def deposit account, amt
    if account.downcase == "savings"
      @savings_balance += amt
      puts "successfully added, #{amt} to your account"
      puts "your new #{account} balance is #{@savings_balance}"
    elsif account.downcase == "checking"
      @checking_balance += amt
      puts "successfully added, #{amt} to your account"
      puts "your new #{account} balance is #{@checking_balance}"
    else
      raise AccountError.new(account)
    end
  end



  def withdraw account, amt
    if account.downcase == "savings"
      if @savings_balance >= amt
        @savings_balance -= amt
        return amt
      else
        raise InsufficientFunds.new
      end
    elsif account.downcase == "checking"
      if @checking_balance >= amt
        @checking_balance -= amt
        return amt
      else
        raise InsufficientFunds.new
      end
    else
      raise AccountError.new(account)
    end
  end



  def account_balances
    puts "your checking account balance #{@checking_balance}"
    puts "your savings account balance #{@savings_balance}"
    puts "your total balance: #{@checking_balance = @savings_balance}"
  end



  # ------------ Custom Error Messages
  class InsufficientFunds < StandardError
    attr_reader :message
    @message = "You're account has insufficient funds"
  end

  class AccountError < StandardError
    attr_reader :message
    def initialize name
      @message = "#{name} is not a valid account name"
    end
  end



  private :generate_account_number

end

bankAccount1 = BankAccount.new
puts bankAccount1.account_number
puts bankAccount1.checking_balance

bankAccount1.account_info
