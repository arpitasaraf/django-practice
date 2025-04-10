console.log("Javascript is running")

const x = 5 + 10
console.log(x)

const btn = document.querySelector('#btn')
const text = document.querySelector(".blue")

console.log(btn)
console.log(text)

btn.addEventListener("click",()=>{
    text.style.color = 'red'
})