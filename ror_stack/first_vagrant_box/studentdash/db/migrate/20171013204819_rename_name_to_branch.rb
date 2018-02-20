class RenameNameToBranch < ActiveRecord::Migration
  def change

  rename_column :dojos, :name, :branch

  end
end
