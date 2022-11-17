*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nolla
    Set Password  nolla000
    Set Password Confirmation  nolla000
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  no
    Set Password  nolla000
    Set Password Confirmation  nolla000
    Submit Credentials
    Registration Should Fail With Message  Username too short
    
Register With Valid Username And Too Short Password
    Set Username  nolla
    Set Password  nolla00
    Set Password Confirmation  nolla00
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  nolla
    Set Password  nolla000
    Set Password Confirmation  nolla1111
    Submit Credentials
    Registration Should Fail With Message  Passwords not matching

Login After Successful Registration
# ...

Login After Failed Registration
# ...

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmatio}
    Input Password  password_confirmation  ${password_confirmatio}
