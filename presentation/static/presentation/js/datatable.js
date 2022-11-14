$(document).ready(function(){

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


// ******************* GESTION DES AFFICHAGES DES CHAMPS STATUT MATRIMONIAL *****************************
    var parent_annuler = $('#parent_annuler');
    var parent_liste = $('#parent_liste');

    parent_annuler.click(function(){
        parent_liste.html('');
    });


// ******************* GESTION DES LISTES DEROULANTES *****************************

    var select_district = $('select[name=select_district]');
    var select_region = $('select[name=select_region]');
    var select_departement = $('select[name=select_departement]');
    var select_ville = $('select[name=select_ville]');
    var select_commune = $('select[name=select_commune]');

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

                    $.each(data.data, function(key, value){
                        select_commune.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });

        });


// ******************* GESTION DES AFFICHAGES DU CHAMP DATE DE NAISSANCE *****************************
    var label_naissance = $('#label_naissance');
    var label_naissance_times = $('#label_naissance_times');
    var label_naissance_plus = $('#label_naissance_plus');
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
        if(select_commune.val()){
            label_naissance.val($('select[name=select_commune] option:selected').text());
            lieu_naissance.val(select_commune.val());
            date_de_naissance_Modal.hide('slow');
            naissance_btn_fermer.trigger('click');
        }
    });


// ******************* GESTION AJAX DE L'AJOUT D'UNE COOPERATIVE *****************************

    var cooperative_a_ajouter = $('#cooperative_a_ajouter');
    var cooperative_a_fermer = $('#cooperative_a_fermer');

        // Traitement AJAX
        cooperative_a_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/vieprofessionnelle/ajouter-cooperative", // On ajoute l'url absolue en commençant par la racine
                type: 'post',
                data: {
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
                    cooperative_a_fermer.trigger('click');
                },
            });


        });


});