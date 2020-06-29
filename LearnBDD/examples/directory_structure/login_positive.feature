Feature: Logging in with valid credentials

  Scenario: User logs in successfully
    Given i create a new user
    When i type mail id
    When i type password
    When i click 'Login'
    Then i should see the text welcome

  Scenario: User logs in with wrong password
    Given i create a new user
    When i type mail id
    When i type wrong password
    When i click 'Login'
    Then i should see the 'Invalid Username/Password Entered' message