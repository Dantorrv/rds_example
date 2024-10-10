function consult_user(){

    let id = document.getElementById("idnum").value
    fetch('/consult_user',{
        'method': 'post',
        'headers': {'Content-type': 'application/json'},
        'body': JSON.stringify(id)

    })
    .then(resp => resp.json())
    .then(data =>{
        document.getElementById("data").value = data.first_name+" "+data.last_name+" "+data.birthday
    })
    .catch(error => alert("error"))
}