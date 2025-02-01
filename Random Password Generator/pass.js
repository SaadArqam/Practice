function generatePassword(length,includeLowercase,includeUppercase,includeNumbers,includeSymbols){
    const lowercaseChars="abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars="0123456789";
    const symbolChars="!@#$%^&*_-";
    let allowedChars="";
    let password="";
    allowedChars+=includeLowercase?lowercaseChars:"";
    allowedChars+=includeUppercase?uppercaseChars:"";
    allowedChars+=includeNumbers?numberChars:"";
    allowedChars+=includeSymbols?symbolChars:"";
    if (length<=0){
        return `(password length must be atleast 1)`;
    }
    if(allowedChars.length===0){
        return `(At least 1 set of characters needs to be selected)`;
    }
    for(let i=0;i<length;i++){
        const randonIndex=Math.floor(Math.random()*allowedChars.length);
        password+=allowedChars[randonIndex];
    }
    return password;
}
const passwordLength=12;
const includeLowercase=true;
const includeUppercase=true;
const includeNumbers=true;
const includeSymbols=true;
const password=generatePassword(passwordLength,includeLowercase,includeUppercase,includeNumbers,includeSymbols);
console.log(`GEnerated Password: ${password}`);

function generateAndDisplayPassword() {
    const length=parseInt(document.getElementById("length").value);
    const includeLowercase=document.getElementById("lowercase").checked;
    const includeUppercase=document.getElementById("uppercase").checked;
    const includeNumbers=document.getElementById("numbers").checked;
    const includeSymbols=document.getElementById("symbols").checked;
    
    const password=generatePassword(length,includeLowercase,includeUppercase,includeNumbers,includeSymbols);
    document.getElementById("password").textContent = password;
}