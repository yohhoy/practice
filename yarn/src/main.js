import { hello } from "./hello.js";

let text = document.createTextNode(hello());
document.getElementById("main").appendChild(text);
