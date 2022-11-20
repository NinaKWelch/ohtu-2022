*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nolla
    Set Password  nolla000
    Set Password Confirmation  nolla000
    Submit Register Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  no
    Set Password  nolla000
    Set Password Confirmation  nolla000
    Submit Register Credentials
    Registration Should Fail With Message  Username too short
    
Register With Valid Username And Too Short Password
    Set Username  nolla
    Set Password  nolla00
    Set Password Confirmation  nolla00
    Submit Register Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  nolla
    Set Password  nolla000
    Set Password Confirmation  nolla1111
    Submit Register Credentials
    Registration Should Fail With Message  Passwords not matching

Login After Successful Registration
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Register Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password
