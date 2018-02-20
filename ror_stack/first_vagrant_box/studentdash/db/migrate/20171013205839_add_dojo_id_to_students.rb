class AddDojoIdToStudents < ActiveRecord::Migration
  def change
    add_column :students, :dojo_id, :integer
    add_index :students, :dojo_id
  end
end
