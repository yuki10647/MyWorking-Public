// let 代入可能   const 代入不可能
// addEventListener 特定のイベントが起きた時の処理



// comment
const form = document.getElementById("form"); //id="form" を取る
const input = document.getElementById("input");  //id="input" を取る
const ul = document.getElementById("ul");   //id="ul" を取る
const todos = JSON.parse(localStorage.getItem("todos"));  // ローカルストレージの要素を取り出す

if(todos){                       // todosが空じゃないならliを作る
    todos.forEach(todo => {
        add(todo);               // liを作成保存
    })
}

form.addEventListener("submit",        //submitされたとき(Enter押されたときの処理)
 function(event){                      // 関数にeventをとれる
    event.preventDefault();            //ブラウザのリロードの中断
    add();                             // add関数を呼び出す
});

function add(todo){                    // li を作成・追加
    let todoText = input.value;        // 入力内容を変数で受け取る

    if(todo){                        // オブジェクトを利用
        todoText = todo.text;
    }

    if(todoText){                                    // 1文字以上入力されていたら保存する
        const li = document.createElement("li");   // liタグを作る
        li.innerText = todoText;                   // todo.text を取得
        li.classList.add("list-group-item");       // 名前を付けてリストに追加

        if(todo && todo.completed){                 // リロードしても線をつけたまま
            li.classList.add("text-decoration-line-through");
        }

        li.addEventListener("contextmenu",        // 右クリック検知
        function(event){
            event.preventDefault();               // メニュー出すのを取り消す
            li.remove();                          // 要素を取り消す
            saveData();                           // 保存
        });

        li.addEventListener("click",              // クリック検知
        function(){
            li.classList.toggle("text-decoration-line-through"); //toggleは切り替えるコマンド 線をつけたり消したり
            saveData();             //保存
        })

        ul.appendChild(li);               // htmlにあるulの子供としてli を取るようにする
        input.value = "";                 // 入力したものをリセット
        saveData();                       // ローカルデータに保存する
    }
}

function saveData(){                            //データを保存する関数
    const lists = document.querySelectorAll("li");  // liタグ全部取って来る
    let todos = [];                                 //空配列
    lists.forEach(list => {                        // 配列の全要素に対する繰り返し処理
        let todo = {                             // オブジェクト
            text: list.innerText,                
            completed: list.classList.contains("text-decoration-line-through")  //完了状態か判定
        };
        todos.push(todo);                        // list.innerText リストの要素と完了状態を保存する
    });
    localStorage.setItem("todos", JSON.stringify(todos));  // ブラウザに要素を保存する。"todos"配列をJSONに変換保存
}