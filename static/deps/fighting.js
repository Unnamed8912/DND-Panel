function addEnemy(){
    enemie_name = document.getElementById('enemy_name').value;
    enemie_hp = document.getElementById('enemy_hp').value;
    parent = document.getElementById('enemies-items-wrapper');
    child = document.createElement("div");
    child.classList.add('enemies-items');
    child.innerHTML = enemie_name + ' | ' + enemie_hp + ' хп' + ' | ' + "<p1 class='initInner'>12</p1> ";
    parent.appendChild(child);
}

let generate_button = document.getElementById('generate_button');
let start_div = document.getElementById('start-fight-div');
let queue = document.getElementById('queue');

function generateInit(){
        let inits = document.getElementsByClassName('initInner');       
        for(let i = 0; i < inits.length; i++){
            inits[i].innerHTML = Math.floor(Math.random() * 20 + 1);
        }
        generate_button.classList.add('hidden');
        start_div.classList.remove('hidden');
    }
function startFight(){
        start_div.classList.add('hidden');
        queue.classList.remove('hidden');
    }