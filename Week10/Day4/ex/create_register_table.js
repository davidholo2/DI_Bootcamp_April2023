exports.up = function(knex) {
    return knex.schema.createTable('register', function(table) {
      table.increments('user_id').primary();
      table.string('first_name');
      table.string('last_name');
      table.string('email').unique();
      table.string('username');
      table.string('password');
      table.timestamp('created_date').defaultTo(knex.fn.now());
      table.timestamp('last_login_date');
    });
  };
  
  exports.down = function(knex) {
    return knex.schema.dropTable('register');
  };
  