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

function deleteTable(){
    const table = document.getElementById("args-table");
    table.innerHTML = "";
}

function createHeader(data){

    const table = document.getElementById("args-table");

    const header = document.createElement("tr");

    for(const primitive of data.variables){
        const th = document.createElement("th");
        th.textContent = primitive;
        header.appendChild(th);
    }

    for(const premise of data.premisas){
        const th = document.createElement("th");
        th.textContent = premise;
        header.appendChild(th);
    }

    const th = document.createElement("th");
    th.textContent = data.conclusion;
    header.appendChild(th);

    table.appendChild(header);
}

function createBody(data){

    const table = document.getElementById("args-table");

    let row_num = data.ans_list.length;

    for(let i = 0; i < row_num; i++){
        const tr = document.createElement("tr");

        const comb = data.combination_list[i];

        for(const v of data.variables){
            const td = document.createElement("td");
            td.textContent = comb[v] ? "V" : "F";
            tr.appendChild(td);
        }

        const ans = data.ans_list[i];

        for(val of ans){
            const td = document.createElement("td");
            td.textContent = val ? "V" : "F";
            tr.appendChild(td);
        }

        if(data.critic_index_list.includes(i)){
            tr.classList.add("critic_row");
        }

        if(data.invalid_index_list.includes(i)){
            tr.classList.add("invalid_row");
        }

        table.appendChild(tr);
    }
}

function makeTable(data){
   let row_num = data.ans_list.length;
   for(let i = 0; i < row_num; i++){
    console.log(data.ans_list[i])
   }
   createHeader(data);
   createBody(data);
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

   if(data.error){
        window.alert(data.message);
        return;
    }

   deleteTable();

   makeTable(data);
}

function main(){
    let addBtn = document.querySelector('#prem-add-button');
    let rmvBtn = document.querySelector('#prem-remove-button');
    let sndBtn = document.querySelector('#args-upload');

    addBtn.addEventListener('click', premContainerAdd);
    rmvBtn.addEventListener('click', premContainerRemove);
    sndBtn.addEventListener('click', argSend);
}

window.addEventListener('load', main);