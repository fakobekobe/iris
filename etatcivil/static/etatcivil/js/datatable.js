$(document).ready(function() {

//******************** SCRIPT DE L'ONGLET TYPE DE PIECE **********************************************
    // Ajout du champ du champ de recherche
    var tabletypepiece = "tabletypepiece";
    var colonnetypepiece = [0,1,2];
    //$('#' + tabletypepiece + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabletypepiece + ' thead' );
    var table1 = $('#' + tabletypepiece ).DataTable( {

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
            columns: colonnetypepiece,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnetypepiece,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnetypepiece,
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
            columns: colonnetypepiece,
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

//******************** SCRIPT DE L'ONGLET NIVEAU **********************************************
    // Ajout du champ du champ de recherche
    var tableniveau = "tableniveau";
    var colonneniveau = [0,1];
    //$('#' + tableniveau + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tableniveau + ' thead' );
    var table2 = $('#' + tableniveau ).DataTable( {

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
            columns: colonneniveau,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneniveau,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonneniveau,
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
            columns: colonneniveau,
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

//******************** SCRIPT DE L'ONGLET NIVEAU SCOLAIRE **********************************************
    // Ajout du champ du champ de recherche
    var tableniveauscolaire = "tableniveauscolaire";
    var colonneniveauscolaire = [0,1,2];
    //$('#' + tableniveauscolaire + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tableniveauscolaire + ' thead' );
    var table3 = $('#' + tableniveauscolaire ).DataTable( {

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
            columns: colonneniveauscolaire,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneniveauscolaire,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonneniveauscolaire,
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
            columns: colonneniveauscolaire,
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

//******************** SCRIPT DE L'ONGLET SEXE **********************************************
    // Ajout du champ du champ de recherche
    var tablesexe = "tablesexe";
    var colonnesexe = [0,1,2];
    //$('#' + tablesexe + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablesexe + ' thead' );
    var table4 = $('#' + tablesexe ).DataTable( {

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
            columns: colonnesexe,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnesexe,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnesexe,
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
            columns: colonnesexe,
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

//******************** SCRIPT DE L'ONGLET NATIONALITE **********************************************
    // Ajout du champ du champ de recherche
    var tablenationalite = "tablenationalite";
    var colonnenationalite = [0,1,2,3];
    //$('#' + tablenationalite + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablenationalite + ' thead' );
    var table5 = $('#' + tablenationalite ).DataTable( {

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
            columns: colonnenationalite,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnenationalite,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnenationalite,
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
            columns: colonnenationalite,
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

//******************** SCRIPT DE L'ONGLET SITUATION MATRIMONIALE **********************************************
    // Ajout du champ du champ de recherche
    var tablesituation = "tablesituation";
    var colonnesituation = [0,1];
    //$('#' + tablesituation + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablesituation + ' thead' );
    var table6 = $('#' + tablesituation ).DataTable( {

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
            columns: colonnesituation,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnesituation,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnesituation,
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
            columns: colonnesituation,
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

} );