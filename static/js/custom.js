$('.img-modal').click(function(event){
    var p = $(this).attr('product-name')
    $('#'+p).modal('show');
});
