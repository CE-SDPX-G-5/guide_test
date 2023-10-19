*** Settings ***
Library             RequestsLibrary

*** Keywords ***
Get next2 JSON
    [Arguments]    ${i}
    ${resp} =   GET     http://127.0.0.1:5000/next2/${i}
    Should Be Equal     ${resp.status_code}     ${200}
    [return]    ${resp.json()}

*** Test Case ***
Test INT
    ${json_resp}=   Get next2 JSON    ${5}
    Should Be Equal     ${json_resp['msg']}     ${7}
    
Test NEGINT
    ${json_resp}=   Get next2 JSON    ${-5}
    Should Be Equal     ${json_resp['msg']}     ${-3}

Test FLOAT
    ${json_resp}=   Get next2 JSON    ${3.5}
    Should Be Equal     ${json_resp['msg']}     ${5.5}

Test ALPHA
    ${json_resp}=   Get next2 JSON    ${'a'}
    Should Be Equal     ${json_resp['msg']}     ${'error'}    