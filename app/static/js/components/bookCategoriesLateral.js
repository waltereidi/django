
$(document).ready(()=>{
    mapCategoriesUrl()

})


function mapCategoriesUrl()
{
    $("[attr-bookCategoriesLateral]").each(function() {
        $(this).click( e => redirectTo($(this).attr('attr-bookCategoriesLateral'))) ;
      });
}
function redirectTo(categoryName)
{
    var url = new URL(window.location.href); 
    url.pathname = `/biblioteca?${categoryName}`
    console.log(`${url}${url.search}`)
    //window.location.href= `${url}${url.search}`;
}