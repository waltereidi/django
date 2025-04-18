$(document).ready(()=>{
    initializeUrls()

})

function initializeUrls()
{
    $('[attr-urlCategory]').each((el , o ) =>{
         source = $(o).attr('attr-urlSource')
         categoryName = $(o).attr('attr-urlCategory')
        $(this).click( (e)=>{ 
            switch(source){
                case 'menu' : urlFromNavMenu(e ,  categoryName ); break ; 
                case 'lateralMenu': urlFromLateralMenu(e , urlFromLateralMenu(e ,categoryName)  ); break; 
                default : new Error("Invalid Option")
            }

        })
    })
}

// function urlCategoryElementClick(e , source , categoryName )
// {
//     e.stopImmediatePropagation()
//     console.log(source)


// }
function urlFromLateralMenu(e, categoryName) 
{
    e.stopImmediatePropagation()
    console.log(categoryName)   
} 
function urlFromNavMenu(e, categoryName )
{

}
