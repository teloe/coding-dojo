class RpgController < ApplicationController

  def index
    unless session[:gold]
      session[:gold] = 0
    end
    unless session[:activities]
      session[:activities] = []
    end
    @gold = session[:gold]
    @activities = session[:activities].reverse_each
    p @activities
  end

  def create
    if params[:building] == 'farm'
      new_gold = Random.rand(10..20)
      session[:gold] += new_gold
    elsif params[:building] == 'cave'
      new_gold = Random.rand(5..10)
      session[:gold] += new_gold
    elsif params[:building] == 'house'
      new_gold = Random.rand(2..5)
      session[:gold] += new_gold
    elsif params[:building] == 'casino'
      new_gold = Random.rand(-50..50)
      session[:gold] += new_gold
    end

    if new_gold > 0
      session[:activities] << {won: 'true', message: "You won #{new_gold}"}
    else
      session[:activities] << {won: 'false', message: "You lost #{new_gold}"}
    end

    redirect_to '/'
  end

end
