const num=document.getElementById("num");
const button=document.getElementById("button");
let max=1000;
let min=0;
let random_num;
button.onclick=function(){
    random_num=Math.floor((Math.random()*max)+min);
    num.textContent=random_num
}