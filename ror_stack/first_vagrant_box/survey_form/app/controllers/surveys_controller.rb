class SurveysController < ApplicationController

  def new
  end

  def submit
    if session.key?("count")
      session[:count] += 1
    else
      session[:count] = 0
    end
    flash[:message] = "Thank you for submitting! The survey has been submitted #{session[:count]} times!"
    session[:name] = params[:name]
    session[:location] = params[:location]
    session[:language] = params[:language]
    session[:comment] = params[:comment]
    p "**** params"
    p params
    p "**** session"
    p session
    redirect_to '/result'
  end

  def result
  end

end
