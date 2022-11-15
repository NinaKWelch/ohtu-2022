*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nolla  nolla000
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  nolla000
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  nolla000
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  nolla  nolla00
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nolla  nollaaaa
    Output Should Contain  Password must contain numbers or special characters

Register With Username Containing Other Characters And Valid Password
    Input Credentials  nolla000  nolla000
    Output Should Contain  Username must only contain letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command