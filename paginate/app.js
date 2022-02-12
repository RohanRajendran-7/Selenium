var tableData = [{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal1',
        'product_link': 'link'
    },
    {
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal2'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal3'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal4'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },{
        'first_name': 'Russell',
        'last_name': 'Wilson',
        'rank': '1',
        'col':'colVal'
    },
]


/*
	1 - Loop Through Array & Access each value
  2 - Create Table Rows & append to table
*/


var state = {
    'querySet': tableData,

    'page': 1,
    'rows': 5,
    'window': 5,
}

buildTable()

function pagination(querySet, page, rows) {

    var trimStart = (page - 1) * rows
    var trimEnd = trimStart + rows

    var trimmedData = querySet.slice(trimStart, trimEnd)

    var pages = Math.round(querySet.length / rows);

    return {
        'querySet': trimmedData,
        'pages': pages,
    }
}

function pageButtons(pages) {
    var wrapper = document.getElementById('pagination-wrapper')

    wrapper.innerHTML = ``
	console.log('Pages:', pages)

    var maxLeft = (state.page - Math.floor(state.window / 2))
    var maxRight = (state.page + Math.floor(state.window / 2))

    if (maxLeft < 1) {
        maxLeft = 1
        maxRight = state.window
    }

    if (maxRight > pages) {
        maxLeft = pages - (state.window - 1)
        
        if (maxLeft < 1){
        	maxLeft = 1
        }
        maxRight = pages
    }
    
    

    for (var page = maxLeft; page <= maxRight; page++) {
    	wrapper.innerHTML += `<button value=${page} class="page btn btn-sm btn-info">${page}</button>`
    }

    if (state.page != 1) {
        wrapper.innerHTML = `<button value=${1} class="page btn btn-sm btn-info">&#171; First</button>` + wrapper.innerHTML
    }

    if (state.page != pages) {
        wrapper.innerHTML += `<button value=${pages} class="page btn btn-sm btn-info">Last &#187;</button>`
    }

    $('.page').on('click', function() {
        $('#table-body').empty()

        state.page = Number($(this).val())

        buildTable()
    })

}


function buildTable() {
    var table = $('#table-body')

    var data = pagination(state.querySet, state.page, state.rows)
    var myList = data.querySet

    for (var i = 1 in myList) {
        //Keep in mind we are using "Template Litterals to create rows"
        var row = `<tr>
                  <td>${myList[i].rank}</td>
                  <td>${myList[i].first_name}</td>
                  <td>${myList[i].last_name}</td>
                  <td>${myList[i].col}</td>
                  <td>${myList[i].product_link}</td>
                  `
        table.append(row)
    }

    pageButtons(data.pages)
}


$(document).ready(function(){
	$(".search-parameters button").click(function(){
		var value = $(this).html()+" : ";
        var input = $('.form-control');
        input.val(value);
	});
});