
document.getElementById("add-submit").addEventListener("click", (e) => {
    // ボタンイベントのキャンセル
    e.preventDefault()
    // データ送信
    let data = new FormData(document.getElementById('upload')) // フォームデータを一括取得(inputタグにname属性が必須です。)
    
    fetch('/up/', { method: 'POST', body: data, }).then(function (response) {
        document.getElementById('message-container').innerHTML = "データ登録完了"
    })
})

