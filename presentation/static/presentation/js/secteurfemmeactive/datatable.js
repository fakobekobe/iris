$(document).ready(function(){

// ******************* GESTION DES SEXES **************

    var sexes = $('input[name=sexe]');
    var nomjeunefille = $('#nomjeunefille');

    sexes.each(function(){
        $(this).change(function(){
            if($(this).val() == 'M'){
                nomjeunefille.attr('style','display:none;');
            }else{
                nomjeunefille.attr('style','display:block;');
            }
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

                    $.each(data.data, function(key, value){
                        select_quartier.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });


// ******************* GESTION DES AFFICHAGES DU CHAMP DATE DE NAISSANCE *****************************
    var label_naissance = $('#label_naissance');
    var label_naissance_times = $('#label_naissance_times');
    var naissance_btn_ajouter = $('#naissance_btn_ajouter');
    var lieu_naissance = $('#lieu_naissance');
    var date_de_naissance_Modal = $('#date_de_naissance_Modal');
    var naissance_btn_fermer = $('#naissance_btn_fermer');

    label_naissance_times.click(function(){
        label_naissance.val('');
        lieu_naissance.val('');
    });

    naissance_btn_ajouter.click(function(e){
        e.preventDefault();
        select_commune.each(function(){
            if($(this).val()){
                $('select[name=select_commune] option:selected').each(function(n,v){
                    if(n == 0){
                        label_naissance.val($(this).text());
                    }
                });
                lieu_naissance.val($(this).val());
                date_de_naissance_Modal.hide('slow');
                naissance_btn_fermer.trigger('click');
            }

        });
    });

// ******************* GESTION DES AFFICHAGES DU CHAMP VILLE *****************************
    var ville_texte = $('#ville_texte');
    var label_ville_times = $('#label_ville_times');
    var ville_btn_ajouter = $('#ville_btn_ajouter');
    var ville = $('#ville');
    var ville_Modal = $('#ville_Modal');
    var ville_btn_fermer = $('#ville_btn_fermer');

    label_ville_times.click(function(){
        ville_texte.val('');
        ville.val('');
    });

    ville_btn_ajouter.click(function(e){
        e.preventDefault();
        select_ville.each(function(){
            if($(this).val()){
                $('select[name=select_ville] option:selected').each(function(n,v){
                    if(n == 1){
                        ville_texte.val($(this).text());
                    }
                });
                ville.val($(this).val());
                ville_Modal.hide('slow');
                ville_btn_fermer.trigger('click');
            }

        });
    });

// ******************* GESTION AJAX DE L'AJOUT D'UNE COOPERATIVE *****************************

    var cooperative_a_ajouter = $('#cooperative_a_ajouter');
    var cooperative_a_fermer = $('#cooperative_a_fermer');
    var cooperative_a_annuler = $('#cooperative_a_annuler');
    var cooperative_l_fermer = $('#cooperative_l_fermer');

    var label_cooperative_times = $('#label_cooperative_times');
    var cooperative = $('#cooperative');
    var cooperative_texte = $('#cooperative_texte');

        // On vide les champs
        label_cooperative_times.click(function(){
            cooperative.val("");
            cooperative_texte.val("");
        });

        // Traitement AJAX
        cooperative_a_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/vieprofessionnelle/ajouter-cooperative", // On ajoute l'url absolue en commençant par la racine
                type: 'post',
                data: {
                    id_json: $('#id_json').val(),
                    nom_cooperative: $('#nom_cooperative').val(),
                    presidente: $('#presidente').val(),
                    contact_presidente: $('#contact_presidente').val(),
                    speculation_agricole: $('#speculation_agricole').val(),
                    superficie_en_culture: $('#superficie_en_culture').val(),
                    superficie_en_production: $('#superficie_en_production').val(),
                    gps_longitude: $('#gps_longitude').val(),
                    gps_latitude: $('#gps_latitude').val(),
                    dateenre: $('#dateenre').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(data){

                    // On remplit les champs
                    cooperative.val(data.data.id);
                    cooperative_texte.val(data.data.cooperative);

                    // Affichage du message
                    alert(data.data.message);

                    // Gestion des fermetures des boutons
                    cooperative_a_annuler.trigger('click'); // On initialise les champs du modal en cours
                    cooperative_a_fermer.trigger('click'); // On ferme le modal en cours
                    cooperative_l_fermer.trigger('click'); // On ferme le modal de la recherche
                },
                statusCode: {
                    404: function(data){
                            alert('Veuillez renseigner les champs SVP.');
                         },
                    400: function(data){
                            alert('Cette coopérative existe déjà.');
                         },
                },
            });


        });

    // Partie 2 : GESTION DU TABLEAU COOPERATIVE

    var liens = $("#table_recherche_cooperative tbody td a");
        liens.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 cooperative.val($(this).attr('value')); // On récupère le id du Secteur Agricole
                 cooperative_texte.val($(this).text()); // On affiche le nom de la coopérative
                 cooperative_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });

// ******************* GESTION DES AFFICHAGES DU CHAMP LIEU D'HABITATION *****************************
    var label_lieu_habitation = $('#label_lieu_habitation');
    var lieu_habitation_times = $('#lieu_habitation_times');
    var lieu_btn_ajouter = $('#lieu_btn_ajouter');
    var lieu_habitation = $('#lieu_habitation');
    var lieu_habitation_Modal = $('#lieu_habitation_Modal');
    var lieu_btn_fermer = $('#lieu_btn_fermer');

    lieu_habitation_times.click(function(){
        label_lieu_habitation.val('');
        lieu_habitation.val('');
    });

    lieu_btn_ajouter.click(function(e){
        e.preventDefault();

        if(select_quartier.val()){
            label_lieu_habitation.val($('#select_quartier option:selected').text());
            lieu_habitation.val(select_quartier.val());
            lieu_habitation_Modal.hide('slow');
            lieu_btn_fermer.trigger('click');
        }

    });

// ******************* GESTION AJAX DE L'AJOUT D'UN CHAPEAU *****************************
    var chapeau_l_fermer = $('#chapeau_l_fermer');

    var label_chapeau_times = $('#label_chapeau_times');
    var chapeau = $('#chapeau');
    var chapeau_texte = $('#chapeau_texte');

    // On vide les champs
    label_chapeau_times.click(function(){
            chapeau.val("");
            chapeau_texte.val("");
        });

    // Partie 2 : GESTION DU TABLEAU CHAPEAU

    var liens_a = $("#table_chapeau tbody td a");
        liens_a.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 chapeau.val($(this).attr('value')); // On récupère le id de la personne ressource
                 chapeau_texte.val($(this).text()); // On affiche le chapeau
                 chapeau_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });

//******************** SCRIPT DE LA PAGINATION TABLEAU CHAPEAU **********************************************
    function f_table_pr(){
        var table_chapeau = $('#table_chapeau' );

        var table10 = table_chapeau.DataTable( {

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
           // Fin de pagination

        } );

        // Recherche globale du tableau
        $('#recherche_chapeau').keyup(function(){
            table10.search($(this).val()).draw();
        });
    }

    f_table_pr(); // On appelle la fonction


// ******************* GESTION AJAX DE L'AJOUT D'UNE PERSONNE RESSOURCE *****************************
    var pr_l_fermer = $('#pr_l_fermer');

    var label_pr_times = $('#label_pr_times');
    var personne_ressource = $('#personne_ressource');
    var personne_r_texte = $('#personne_r_texte');

    // On vide les champs
    label_pr_times.click(function(){
            personne_ressource.val("");
            personne_r_texte.val("");
        });

    // Partie 2 : GESTION DES TABLEAUX PERSONNES RESSOURCES

    var liens_a = $("#table_recherche_personneressource tbody td a");
        liens_a.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 personne_ressource.val($(this).attr('value')); // On récupère le id de la personne ressource
                 personne_r_texte.val($(this).text()); // On affiche le chapeau
                 pr_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });

    var liens_a_m = $("#table_recherche_personneressource_m tbody td a");
        liens_a_m.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 personne_ressource.val($(this).attr('value')); // On récupère le id de la personne ressource
                 personne_r_texte.val($(this).text()); // On affiche le chapeau
                 pr_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });

// GESTION DE L'AFFICHAGE DES TABLES PERSONNES RESSOURCES ********************
    var type_pr = $('#select_typepersonneressource');
    var trc = $('#trc');
    var trm = $('#trm');
    type_pr.change(function(){

            if(trc.attr('value') == $(this).val()){
                // On traitre le cas du Chapeau
                trm.removeClass('db');
                trm.addClass('dn');

                trc.removeClass('dn');
                trc.addClass('db');

            }else{
                // On traitre le cas du membre
                trc.removeClass('db');
                trc.addClass('dn');

                trm.removeClass('dn');
                trm.addClass('db');
            }


        });

//******************** SCRIPT DE LA PAGINATION DES TABLEAUX PERSONNES RESSOURCES **********************************************
    function f_table_r_pr(){
        var table_recherche_pr = $('#table_recherche_personneressource' );
        var colonnerecherche_personneressource = [0,1,2];

        var table10 = table_recherche_pr.DataTable( {

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
           // Fin de pagination

        } );

        // Recherche globale du tableau
        $('#recherche_personneressource').keyup(function(){
            table10.search($(this).val()).draw();
        });
    }

    f_table_r_pr(); // On appelle la fonction

    function f_table_r_pr2(){
        var table_recherche_pr = $('#table_recherche_personneressource_m' );
        var colonnerecherche_personneressource = [0,1,2];

        var table10 = table_recherche_pr.DataTable( {

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
            // Fin de pagination


        } );

        // Recherche globale du tableau
        $('#recherche_personneressource_m').keyup(function(){
            table10.search($(this).val()).draw();
        });
    }

    f_table_r_pr2(); // On appelle la fonction


// CONTROL DE L'ENVOI DES DONNEES ****************************************
    var envoyer_fiche = $('#envoyer_fiche');
    var nom = $('input[name=nom]');
    var date_naissance = $('input[name=date_naissance]');
    var numeropiece = $('input[name=numeropiece]');
    var nationalite = $('select[name=nationalite]');
    var typeresponsabilite = $('#select_typeresponsabilite');
    var montantfinancement = $('#select_montantfinancement');
    var contact = $('input[name=contact]');
    var valider = true;

    envoyer_fiche.click(function(e){
        e.preventDefault();

        if(!nom.val()){
            valider = false;
            alert("Veuillez renseigner le nom.");
            nom.focus();
        }else if(!date_naissance.val()){
            valider = false;
            alert("Veuillez renseigner la date de naissance.");
            date_naissance.focus();
        }else if(!numeropiece.val()){
            valider = false;
            alert("Veuillez renseigner le numéro de la pièce.");
            numeropiece.focus();
        }else if(!nationalite.val()){
            valider = false;
            alert("Veuillez selectionner la nationalité.");
            nationalite.focus();
        }else if(!contact.val()){
            valider = false;
            alert("Veuillez renseigner le contact.");
            contact.focus();
        }else if(!cooperative.val()){
            valider = false;
            alert("Veuillez ajouter une coopérative.");
            cooperative_texte.focus();
        }else if(!typeresponsabilite.val()){
            valider = false;
            alert("Veuillez selectionner le type de responsabilité.");
            typeresponsabilite.focus();
        }else if(!montantfinancement.val()){
            valider = false;
            alert("Veuillez selectionner le montant du financement.");
            montantfinancement.focus();
        }else if(!chapeau.val()){
            valider = false;
            alert("Veuillez ajouter un chapeau.");
            chapeau_texte.focus();
        }else if(!personne_ressource.val()){
            valider = false;
            alert("Veuillez ajouter une personne ressource.");
            personne_r_texte.focus();
        }else if(!niveau.val()){
            valider = false;
            alert("Veuillez selectionner le niveau.");
            niveau.focus();
        }else if(!niveauscolaire.val()){
            valider = false;
            alert("Veuillez selectionner le niveau scolaire.");
            niveauscolaire.focus();
        }else if(!lieu_habitation.val()){
            valider = false;
            alert("Veuillez ajouter le lieu d'habitation.");
            label_lieu_habitation.focus();
        }else{
            valider = true;
        }
        if(valider){
            // On envoi le formulaire
            $('#form_fiche').submit();
        }


    });


// GESTION DE LA PAGINATION DE LA TABLE GROUPEMENT ********************************************************
    var table_recherche_groupement = $('#table_recherche_groupement');
    var table13 = table_recherche_groupement.DataTable( {

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

    } );

    // Recherche globale du tableau
    $('#recherche_groupement').keyup(function(){
        table13.search($(this).val()).draw();
    });




// FIN ***********************************************************************

});