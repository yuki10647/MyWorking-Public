// 変数、定数、配列
// ループ while
// 条件処理
// 関数 functionを使うほうと使わないほう
// オブジェクト
// window.alert()
// document.getElementBy.... などの要素取得用関数
// addEventListener()   イベントを付け加える


// アプリの作成

// 問題の文章、選択肢、答えの3点セットを配列のオブジェクトを用いることで簡潔に書く
const quiz = [
    {
        question: 'ゲーム史上、最も売れたゲーム機はどれ？',
        answers:  [
            'スーパーファミコン',
            'プレイステーション',
            'ニンテンドースイッチ',
            'ニンテンドーDS'
        ],
        correct: 'ニンテンドーDS'
    }, {
        question: '世界一高い山は？',
        answers:  [
            '富士山',
            'エベレスト',
            '北岳',
            '西小山'
        ],
        correct: 'エベレスト'
    }, {
        question: '日本一長い川は？',
        answers:  [
            '信濃川',
            'ミシシッピ川',
            '春の小川',
            'ナイル川'
        ],
        correct: '信濃川'
    }
];
const quizLength = quiz.length;
let quizIndex = 0;
let score = 0;

const $button = document.getElementsByTagName('button');    //buttonは他にないのでTagNameでとってきたほうが良い 配列で取得
const buttonLength = $button.length;

// 表示用の命令を関数にする
const setupQuiz = () => {               // quiz[quizIndex]. は後付け
    //問題文を表示したい
    document.getElementById('js-question').textContent = quiz[quizIndex].question;  //テキストの情報を変える。これでHTMLの表示も変わる

    //選択肢を表示したい
    let buttonIndex = 0;                                 
    let buttonLength = $button.length;
    while(buttonIndex < buttonLength){                                // 配列の要素のテキストを書き換える
        $button[buttonIndex].textContent = quiz[quizIndex].answers[buttonIndex];   
        buttonIndex++;
    }
}
setupQuiz();

//正誤判定用関数
const clickHandler = (e) => {                   //e はイベント　e.target はクリックされたボタン
    //正解。不正解の表示を作りたい
    if(quiz[quizIndex].correct===e.target.textContent) {
        window.alert('正解');
        score++;
    } else {
        window.alert('不正解');
    }
    // 次の問題にいく、終了する
    quizIndex++;
    if(quizIndex < quizLength){
        setupQuiz();
    } else {
        window.alert('終了!あなたの正解数は'+ score + '/' + quizLength + 'です!!!');
    }
};

let handleIndex = 0;                      
while(handleIndex < buttonLength){                   //イベントを付け加える  これを$button[0~3]で繰り返す
    $button[handleIndex].addEventListener('click', (e) => {      
        clickHandler(e);
    });   
    handleIndex++;
}

