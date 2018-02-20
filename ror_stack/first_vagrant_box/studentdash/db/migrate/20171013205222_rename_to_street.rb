class RenameToStreet < ActiveRecord::Migration
  def change
    rename_column :dojos, :address, :street
  end
end
