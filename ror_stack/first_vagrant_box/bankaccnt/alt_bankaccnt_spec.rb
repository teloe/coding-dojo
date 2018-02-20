# To do
# - Has a getter method for retrieving the checking account balance
#
# - Has a getter method that retrieves the total account balance
#
# - Has a function that allows the user to withdraw cash
#
# - Raises an error if a user tries to withdraw more money than they have in the account
#
# - Raises an error when the user attempts to retrieve the total number of bank accounts
#
# - Raises an error when the user attempts to set the interest rate

require_relative 'alt_bankaccnt'
RSpec.describe BankAccount do
  before(:each) do
    @acc = BankAccount.new
  end

  it "has a getter method for retrieving the checking account balance" do
    expect(@acc.checking).to eq(0)
  end

  it "has a getter method that retrieves the total account balance" do
    expect(@acc.total).to eq("Checking Balance: 0\nSavings Balance: 0\nTotal Balance: 0")
  end

  context "withdrawing money" do
    it "raises an error if a user tries to withdraw more money than they have in checking" do
      expect{ @acc.withdraw("checking", 100) }.to raise_error("Insufficient funds!")
    end

    it "raises an error if a user tries to withdraw more money than they have in savings" do
      expect{ @acc.withdraw("savings", 100) }.to raise_error("Insufficient funds!")
    end
  end

  it "raises an error when the user attempts to retrieve the total number of bank accounts" do
    expect{ @acc.number_of_accounts }.to raise_error(NoMethodError)
  end

  it "raises an error when the user attempts to set the interest rate" do
    expect{ @acc.interest_rate }.to raise_error(NoMethodError)
  end

end
