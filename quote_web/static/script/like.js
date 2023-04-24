function like(quoteId){
    const likeCount = document.getElementById(`likes-count-${quoteId}`);
    const likeButton = document.getElementById(`like-button-${quoteId}`);

    fetch(`/like-quote/${quoteId}`, {method: 'POST'})
    .then((res) => res.json())
    .then((data) => {
        likeCount.innerHTML = data['likes'];
        if (data["liked"] === true) {
            likeButton.className = "fa-solid fa-heart";
        } else {
            likeButton.className = "fa-regular fa-heart";
        }
    }).catch((e) => alert("Для данного действия нужно авторизоваться."));


}