$(document).ready(function () {
    $('#submit-vehicle').click(function () {
        var id = $('#create-modal').find('input[id="id"]').val();
        var brand = $('#create-modal').find('input[id="brand"]').val();
        var model = $('#create-modal').find('input[id="model"]').val();
        var price = $('#create-modal').find('input[id="price"]').val();
        var avg = $('#create-modal').find('input[id="avg"]').val();
        var stat = $('#create-modal').find('input[id="stat"]').val();

        console.log($('#create-modal').find('input[id="id"]').val())
        
        $.ajax({
            type: 'POST',
            url:   '/create',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'Vehicle_ID':id,
                'Brand': brand,
                'Model' : model,
                'Price': price,
                'Average_Maintenance_Cost':avg,
                'Upcoming_Current': stat
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#delete-vehicle').click(function () {
        var id = $('#delete-modal').find('.form-control').val();
        console.log($('#delete-modal').find('.form-control').val())

        $.ajax({
                    type: 'POST',
                    url: '/delete',
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                            'Vehicle_ID':id
                     }),
                    success: function (res) {
                        console.log(res.response)
                        location.reload();
                    },
                    error: function () {
                        console.log('Error');
                    }
                });
    });

    $('#search-database').click(function () {
        var key = $('#search-modal').find('.form-control').val();
        console.log($('#search-modal').find('.form-control').val())

        $.ajax({
                    type: 'GET',
                    url: '/search/' + key,
                    success: function (res) {
                        window.open('/search/'+key);
                    },
                    error: function () {
                        console.log('Error');
                    }
                });
                
    });

    $('#search-database-user').click(function () {
        var key = $('#user-search-modal').find('.form-control').val();
        console.log($('#user-search-modal').find('.form-control').val())

        $.ajax({
                    type: 'GET',
                    url: '/search/' + key,
                    success: function (res) {
                        window.open('/search/'+key);
                    },
                    error: function () {
                        console.log('Error');
                    }
                });
                
    });
    $('#employee-login').click(function () {
        var id = $('#employee-modal').find('input[id="employee-id"]').val();
        var password = $('#employee-modal').find('input[id="employee-password"]').val();

        $.ajax({
            type: 'POST',
            url: '/employee-login',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                    'id':id,
                    'password':password
             }),
            success: function (res) {
                window.open('/employeehomepage');

            },
            error: function () {
                console.log('Error');
            }
        });
                
    });


    $('#user-login').click(function() {
        var id = $('#user-modal').find('input[id="user-id"]').val();
        var password = $('#user-modal').find('input[id="user-password"]').val();

        $.ajax({
            type: 'POST',
            url: '/user-login',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                    'id':id,
                    'password':password
             }),
            success: function (res) {
                window.open('/userhomepage');

            },
            error: function () {
                console.log('Error');
            }
        });
                
    });


    $('#update-status').click(function() {
        var brand = $('#update-modal').find('input[id="update-brand"]').val();
        var model = $('#update-modal').find('input[id="update-model"]').val();
        var n_stat = $('#update-modal').find('input[id="update-stat"]').val();

        $.ajax({
            type: 'POST',
            url:   '/update',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                'Brand': brand,
                'Model' : model,
                'Upcoming_Current': n_stat
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#Query1').click(function() {
        var b1 = document.getElementById('Brand-1').value;
        var b2 = document.getElementById('Brand-2').value;

        var c1 = document.querySelector('input[name="C-Type"]:checked').value;
        var c2 = document.querySelector('input[name="C-Type2"]:checked').value;


        $.ajax({
            type: 'GET',
            url: '/customquery1/' + b1 + '/' + c1 + '/' + b2 + '/'+ c2,
            success: function (res) {
                window.open('/customquery1/' + b1 + '/' + c1 + '/' + b2 + '/'+ c2);
            },
            error: function () {
                console.log('Error');
            }
        });

    });


    $('#Query2').click(function() {
        var brand = document.getElementById('bq2').value;
    
        $.ajax({
            type: 'GET',
            url: '/customquery2/' + brand,
            success: function (res) {
                window.open('/customquery2/' + brand);
            },
            error: function () {
                console.log('Error');
            }
        });

    });


    $('#hello').click(function() {
        console.log('Clicked the Button is Registered')
        $.ajax({
                    type: 'GET',
                    url: '/sp',
                    success: function (res) {
                       console.log(Success);
                    },
                    error: function () {
                        console.log('Error');
                    }
                });
                window.open('/sp');
                
    });

});


