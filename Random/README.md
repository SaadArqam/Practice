# Random Number Generator

This project is a simple **Random Number Generator** built using **HTML, CSS, and JavaScript**. It generates a random number between `0` and `1000` when the "GENERATE" button is clicked.

## 🚀 Features
- Generates a random number between `0` and `1000`
- Styled button with hover effect
- Simple and interactive UI
- Lightweight and fast

## 📂 Project Structure
random-number-generator/
│── random.html # Main HTML file
│── random.css # Styles for the page 
│── random.js # JavaScript logic 
│── README.md # Project documentation


## 🛠 Technologies Used
- **HTML** - For structuring the web page  
- **CSS** - For styling the button and layout  
- **JavaScript** - For generating the random number  

## 🎯 How It Works
1. Open `random.html` in a browser.  
2. Click the **"GENERATE"** button.  
3. A random number will be displayed on the screen.  

## 📝 Code Explanation
### **HTML (`index.html`)**
- Defines the layout with a **button** and a **label** for displaying the generated number.

### **CSS (`random.css`)**
- Centers the button and number.
- Adds a hover effect to the button.

### **JavaScript (`random.js`)**
- Uses `Math.random()` to generate a random number.
- Updates the label with the new number on button click.

```js
const num = document.getElementById("num");
const button = document.getElementById("button");
let max = 1000;
let min = 0;
button.onclick = function () {
    let random_num = Math.floor((Math.random() * max) + min);
    num.textContent = random_num;
}

