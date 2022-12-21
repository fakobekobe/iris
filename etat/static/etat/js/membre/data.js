$(document).ready(function(){

// ******************* GESTION AJAX DE LA LISTE DEROULANTE DU SECTEUR D'ACTIVITE *****************************

    var select_typesecteur = $('#typesecteur');
    var select_secteur = $('#secteur');
    var select_activite = $('#activite');

    // Traitement AJAX du niveau
    select_typesecteur.change(function(){
            // On utilise ajax pour récupérer les niveaux
            $.ajax({
                url: "/vieprofessionnelle/details-secteur", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    select_secteur.html('');
                    select_secteur.append("<option value='' selected>--- Sélectionnez un secteur ---</option>");

                    $.each(data.data, function(key, value){
                        select_secteur.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });
            $.ajax({
                url: "/vieprofessionnelle/details-activite", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    select_activite.html('');
                    select_activite.append("<option value='' selected>--- Sélectionnez un nom ---</option>");

                    $.each(data.data, function(key, value){
                        select_activite.append("<option value='" + value.id + "' >" + value.nom + "</option>");
                    });
                },
            });
        });

// ******************* GESTION DES LISTES DEROULANTES *****************************

    var select_district = $('select[name=select_district]');
    var select_region = $('select[name=select_region]');
    var select_departement = $('select[name=select_departement]');
    var select_ville = $('select[name=select_ville]');
    var select_commune = $('select[name=select_commune]');
    var select_quartier = $('select[name=select_quartier]');
    var select_marche = $('select[name=select_marche]');

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

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

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

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

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

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

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

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_commune.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });

        });

        // Traitement AJAX de la quartier
        select_commune.change(function(){

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

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_quartier.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX du marché
        select_quartier.change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-marche", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_marche.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });


// ******************* GESTION DES LISTES DEROULANTES *****************************

    var niveau = $('select[name=niveau]');
    var niveauscolaire = $('select[name=niveauscolaire]');

    // Traitement AJAX du niveau
    niveau.change(function(){
            // On utilise ajax pour récupérer les niveaux
            $.ajax({
                url: "/presentation/details-niveauscolaire", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    niveauscolaire.html('');
                    niveauscolaire.append("<option value='' selected>--- Selectionnez un niveau scolaire ---</option>");

                    $.each(data.data, function(key, value){
                        niveauscolaire.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });
        });

// ------------ CHARGEMENT DES DONNEES DU FORMULAIRE DES ETATS --------------------

var form_membre = $('#form_membre');
var btn_fiche_identification = $('#btn_fiche_identification');
var btn_liste_badge = $('#btn_liste_badge');
    btn_fiche_identification.click(function(e){
        e.preventDefault();
        form_membre.attr('action','/etat/fiche-identification');
        form_membre.submit();
        // On instancie un objet formulaire pour l'envoi des champs du formulaire
        //var formData = new FormData(form_membre[0]);

        /* On utilise ajax pour transmettre les données
        $.ajax({
              url: "/etat/fiche-identification", // On ajoute l'url absolue en commençant par la racine
              type: 'POST',
              data: formData,
              success: function(data){
                    alert(data.data);
              },
              statusCode: {
                 404: function(data){
                     alert('Veuillez réessayer car une erreur est survenue.');
                 },
              },
              cache: false,
              contentType: false,
              processData: false,
        });
        */
    });
    btn_liste_badge.click(function(e){
        e.preventDefault();
        form_membre.attr('action','/etat/liste-badge');
        form_membre.submit();
    });


// PAGINATION DE LA TABLE LISTE N°BADGE **********************************
    var table_recherche_membre = "table_recherche_membre";
    var colonnerecherche = [0,1,2,3,4,5,6];
    var table = $('#' + table_recherche_membre ).DataTable( {

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
                columns: colonnerecherche,
            },
        },

        { // Boutton de excel
            extend:'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            // Option pour le choix des colonnes a afficher
            exportOptions:{
                columns: colonnerecherche,
            },
        },

        { // Boutton PDF
            extend:'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns: colonnerecherche,
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
                columns: colonnerecherche,
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

    } );

    // Recherche globale du tableau
    var monTableau = $('#'+ table_recherche_membre).DataTable(); // On récupère le tableau
    $('#recherche_membre').keyup(function(){
        monTableau.search($(this).val()).draw();
    });

// FIN ****************************************************************************

});