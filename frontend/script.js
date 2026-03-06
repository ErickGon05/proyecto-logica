class premContainer extends HTMLElement{
    constructor(){
        super();
        const shadow = this.attachShadow({mode: 'open'});

        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "style.css";
        shadow.appendChild(link);

        this.input = document.createElement('input');
        this.input.type = "text";
        this.input.placeholder = "premisa";
        this.input.classList.add("container-input");

        shadow.appendChild(this.input);
    }

    getValue(){
        return this.input.value;
    }
}
customElements.define("prem-container", premContainer);

var premArray = [];

function premContainerAdd(){
    let premsWrapper = document.querySelector('#prem-component-container');
    const newPremContainer = document.createElement("prem-container");
    premsWrapper.appendChild(newPremContainer);
    premArray.push(newPremContainer);
}
function premContainerRemove(){
    let ArrLen = premArray.length;
    if(ArrLen == 0) return
    premArray[ArrLen - 1].remove();
    premArray.pop();
}

async function argSend(){
    let aborted = false;
    let argStr = "";
    let conclusion = document.getElementById("conclution-input").value
    console.log(conclusion)
    for(const x of premArray){
        let v = x.getValue();
        for (const i in v){
            if(v[i] == ','){
                window.alert("el uso del caracter ',' esta reservado para el funcionamiento interno de la aplicacion, por favor evite su uso dentro de las entradas de texto");
                aborted = true;
                return;
            }
        };
        argStr.length == 0 ? argStr += `${v}` : argStr += `, ${v}`;
    };
    if(conclusion.length == 0) return;
    if(aborted || argStr.length == 0) return;
    
    const resp = await fetch('/eval', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({premisas: argStr, conclusion: conclusion})
    });
    
   const data = await resp.json();

   console.log(data);
}

function printValues(){
    let values = []
    premArray.forEach((x)=>{
        values.push(x.getValue())
    });
    console.log(values)
}

function main(){
    let addBtn = document.querySelector('#prem-add-button');
    let rmvBtn = document.querySelector('#prem-remove-button');
    let sndBtn = document.querySelector('#args-upload');
    let test = document.querySelector('#test-btn')

    addBtn.addEventListener('click', premContainerAdd);
    rmvBtn.addEventListener('click', premContainerRemove);
    sndBtn.addEventListener('click', argSend);
    test.addEventListener('click', printValues);
}

window.addEventListener('load', main);