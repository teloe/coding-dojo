class BankAccount

  private
  attr_accessor :account_number, :checking, :savings

  @@number_of_accounts = 0

  @@interest_rate = 0.1

  def create_account_number
    rand(10 ** 16)
  end


  public
  def initialize(checking_deposit, savings_deposit)
    @account_number = create_account_number
    @checking = checking_deposit
    @savings = savings_deposit
    @@number_of_accounts += 1
  end


  def deposit(account, amount)
    if account == "checking"
      @checking += amount
    elsif account == "savings"
      @savings += amount
    else
      p "account doesn't exist"
    end
  end


  def withdraw(account, amount)
    if account == "checking"
      if amount > @checking
        p "checking has insufficient funds"
      else
        @checking -= amount
      end
    elsif account == "savings"
      if amount > @savings
        p "savings is dry"
      else
        p @savings -= amount
      end
    else
      p "account doesn't exist"
    end
  end


  def get_total_money
    p @checking + @savings
  end


  def account_info
    p "account number is #{@account_number}"
    p "total money is #{get_total_money}"
    p "checking balance is #{@checking}"
    p "savings balance is #{@savings}"
    p "interest rate is #{@@interest_rate}%"
  end


  def get_checking
    @checking
  end


  def get_savings
    @savings
  end


  def get_account_number
    @account_number
  end

end


mine = BankAccount.new(500, 25)
mine.account_info
# mine.interest_rate
# mine.get_total_money
# mine.withdraw("checking", 300)
p mine.get_checking
p mine.get_savings
p mine.get_account_number
