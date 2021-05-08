function teste(id) {
    this.resultado = window.confirm("Tem certeza que quer usar a dica?");
    if(resultado){
        this.document.getElementById(id).innerHTML= this.document.getElementById(id).value;
    }
}




