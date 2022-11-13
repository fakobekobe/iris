$(document).ready(function() {
//******************** SCRIPT DE L'ONGLET DISTRICT **********************************************
    // Ajout du champ du champ de recherche
    var IdTableau = "district";
    //$('#' + IdTableau + ' thead tr').clone(true).addClass('filters').appendTo( '#' + IdTableau + ' thead' );
    var table1 = $('#' + IdTableau ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
   /* "columnDefs":[{
        "targets":3, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },
    /**
    language: {
        url: '/localisation/fr_FR.json'
    }
    **/


    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2],
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2],
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: [0,1,2],
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2],
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );

    /* Recherche globale du tableau
    var monTableau = $('#'+ IdTableau +'').DataTable(); // On récupère le tableau
    $('#rechercheDatatables').keyup(function(){
        monTableau.search($(this).val()).draw();
    });
     Fin de recherche*/

//******************** SCRIPT DE L'ONGLET REGION **********************************************
     // Ajout du champ du champ de recherche
    var tableregion = "tableregion";
    //$('#' + tableregion + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tableregion + ' thead' );
    var table2 = $('#' + tableregion ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3],
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3],
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: [0,1,2,3],
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3],
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );


//******************** SCRIPT DE L'ONGLET DEPARTEMENT **********************************************
     // Ajout du champ du champ de recherche
    var tabledepartement = "tabledepartement";
    //$('#' + tabledepartement + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabledepartement + ' thead' );
    var table3 = $('#' + tabledepartement ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3,4],
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3,4],
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: [0,1,2,3,4],
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: [0,1,2,3,4],
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );

//******************** SCRIPT DE L'ONGLET VILLE **********************************************
     // Ajout du champ du champ de recherche
    var tableville = "tableville";
    var colonneville = [0,1,2,3,4,5];

    //$('#' + tableville + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tableville + ' thead' );
    var table4 = $('#' + tableville ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneville,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneville,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonneville,
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneville,
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );

//******************** SCRIPT DE L'ONGLET COMMUNE **********************************************
     // Ajout du champ du champ de recherche
    var tablecommune = "tablecommune";
    var colonnecommune = [0,1,2,3,4,5,6];

    //$('#' + tablecommune + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablecommune + ' thead' );
    var table5 = $('#' + tablecommune ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnecommune,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnecommune,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnecommune,
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnecommune,
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );


//******************** SCRIPT DE L'ONGLET QUARTIER **********************************************
     // Ajout du champ du champ de recherche
    var tablequartier = "tablequartier";
    var colonnequartier = [0,1,2,3,4,5,6,7];

    //$('#' + tablequartier + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablequartier + ' thead' );
    var table6 = $('#' + tablequartier ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnequartier,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnequartier,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnequartier,
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnequartier,
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );

//******************** SCRIPT DE L'ONGLET MARCHE **********************************************
     // Ajout du champ du champ de recherche
    var tablemarche = "tablemarche";
    var colonnemarche = [0,1,2,3,4,5,6,7,8];

    //$('#' + tablemarche + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablemarche + ' thead' );
    var table7 = $('#' + tablemarche ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
    dom:'lBfrtip',
    buttons: [

    { // Boutton de copie
        extend:'copy',
        text: '<i class="fas fa-clone"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Copier',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnemarche,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnemarche,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnemarche,
        },

        tableHeader: {
            alignment: 'center',
        },

        customize: function (doc){
            doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
            doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
            doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
            doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
            doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

            // Centrer le tableau dans le document
            doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
        },

    },

    { // Boutton Imprimer
        extend:'print',
        text: '<i class="fas fa-print"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Imprimer',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnemarche,
        },

        // Personnalisation de l'affichage
        customize: function(win){
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        },
    },

    ],

        // Fin de pagination

/*
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns([0,1,2,3]).eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        },*/


    } );

// ******************* GESTION DES LISTES DEROULANTES *****************************

    var select_district = $('select[name=select_district]');
    var select_region = $('select[name=select_region]');
    var select_departement = $('select[name=select_departement]');
    var select_ville = $('select[name=select_ville]');
    var select_commune = $('select[name=select_commune]');
    var select_quartier = $('select[name=select_quartier]');

        // Traitement AJAX de la region
        $(select_district).change(function(){

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/localisation/details-region", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection de la région
                    select_region.html('');
                    select_region.append("<option value='' selected>--- Selectionnez une région ---</option>");

                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    $.each(data.data, function(key, value){
                        select_region.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX du departement
        $(select_region).change(function(){

            // On utilise ajax pour récupérer les départements
            $.ajax({
                url: "/localisation/details-departement", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    $.each(data.data, function(key, value){
                        select_departement.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la ville
        $(select_departement).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-ville", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    $.each(data.data, function(key, value){
                        select_ville.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la commune
        $(select_ville).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-commune", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    $.each(data.data, function(key, value){
                        select_commune.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la quartier
        $(select_commune).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-quartier", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    $.each(data.data, function(key, value){
                        select_quartier.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

// ******************* FIN DE LA GESTION DES LISTES DEROULANTES *****************************

} );