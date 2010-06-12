function CalendarManager(full_calendar, base_url) {
    this.full_calendar = full_calendar;
    this.events_sources = [];
    this.base_url = base_url;
    this.lolilol = "lolilol";
    this.oprhans = [];

    this.EventSource = function(type, base_url, id) {
        this.type = type;
        this.id = id;
        this.base_url = base_url;
        this.displayed = false;


        this.Event = function(fc_event) {
            this.fc_event = fc_event;
        };
        this.events = [];
        this.add_event = function (fc_event) {
            this.events.push(fc_event);
        };

        this.url = function(what) {
            url =  this.base_url + what + "/" + type + "/" + id;
            return url
        }
    }

    this.add_event_source = function (type, id ) {
        name = type+id;
        this.events_sources[name] = (new this.EventSource(type, this.base_url,  id));
    };

    this.edit_event = function(fc_event) {
        this.full_calendar.fullCalendar('removeEvents', fc_event.id);
        this.orphans.push(fc_event);
        this.full_calendar.fullCalendar('renderEvent', fc_event);
    }
    
    this.purge_orphans = function () {
        for(i in this.orphans)
        {
            //Purge the events we added
            to_remove = this.orphans[i].id;
            this.full_calendar.fullCalendar('removeEvents', to_remove);
        }
        this.orphans = [];
    };

    this.purge_event_source = function (name) {
        this.purge_orphans();
        for(i in this.events_sources[name].events)
        {
            //Purge the events we added
            to_remove = this.events_sources[name].events[i].id;
            this.full_calendar.fullCalendar('removeEvents', to_remove);
        }
        this.events_sources[name].events = [];
    };

    this.display_event_source = function(name) {
        if(this.events_sources[name].displayed == false)
        {
            this.purge_event_source(name);
            this.full_calendar.fullCalendar('addEventSource',
            this.events_sources[name].url("get"));
            this.events_sources[name].displayed = true;
        }
    };

    this.hide_event_source = function(name) {
        this.full_calendar.fullCalendar('removeEventSource',
        this.events_sources[name].url("get"));
        this.purge_event_source(name);
        this.events_sources[name].displayed = false;
    };

    this.add_event = function(source_name, fc_event) {
        this.events_sources[source_name].add_event(fc_event);
        this.full_calendar.fullCalendar('renderEvent', fc_event);
    };

}

function CalendarCheckbox(element, fc_manager, type)
{
    if(!type)
        type=""
    element.data("fc_mgr", fc_manager);
    element.data("src_type", element.val());
    element.data("src_real_type", type);
    if(type!="")
        fc_manager.add_event_source(type, element.val());
    else
        fc_manager.add_event_source(element.val(), "");
    element.check_function = function() {
        if(this[0].checked)
            $(this).data("fc_mgr").
            display_event_source($(this).data("src_real_type") +
                                 $(this).data("src_type"))
        else
            $(this).data("fc_mgr").
            hide_event_source($(this).data("src_real_type") +
                                 $(this).data("src_type"))
    };

    element.click(function() {element.check_function()});
    element.check_function();
}

function CalendarSelector(element, source_type, fc_manager)
{
    this.element = element;
    this.source_type = source_type;
    this.fc_manager = fc_manager;
    this.ids = [];

    children = element.children("option").map(function(u, elem) {
        return elem;
        }).get();
    
    for(i in children)
    {
        {
            fc_manager.add_event_source(source_type, children[i].value);
            this.ids.push(children[i].value);
        }
    }
 
    element.data("ids", this.ids);
    element.data("fc_mgr", fc_manager);
    element.data("src_type", source_type);
    element.check_function = function () {
        var ids = $(this).data("ids");
        for(i in ids) {
            mval = $(this).val();
            if($.inArray(ids[i], mval) >= 0)
                $(this).data("fc_mgr").display_event_source($(this)
                                                    .data("src_type")+
                                                    $(this).data("ids")[i])
            else
                $(this).data("fc_mgr").hide_event_source($(this)
                                                    .data("src_type")+
                                                    $(this).data("ids")[i])
        }

    };

    element.change(function() {element.check_function()});
    element.check_function();
}


function CalendarEditor(element, fc_manager, callback)
{
    element.data("fc_mgr", fc_manager);
    element.submiter = function() {
        url = $(this).data("url");
        fc_mgr = $(this).data("fc_mgr");
        $.post(url, $(this).serialize(),
            function(data) {
               fc_mgr.edit_event(data)}, "json");
        if(callback)
            callback();
        return false;
        }

    element.submit(function() {
        return element.submiter();
    });
}


function CalendarSubmiter(element, fc_manager, source_type, callback)
{
    element.data("source_type", source_type);
    element.data("fc_mgr", fc_manager);
    element.submiter = function () {
        url = $(this).data("url");
        fc_mgr = $(this).data("fc_mgr");
        source_type = $(this).data("source_type") 
        selector = $("#id_" + source_type + "-"+source_type).val();
        if(!selector)
            selector = "";
        s_name = source_type + selector;
        url = fc_mgr.events_sources[s_name].url("add");
        $.post(url, $(this).serialize(),
            function(data) {
               fc_mgr.add_event(s_name, data)}, "json");
        if(callback)
            callback();
        return false;
        }
    element.submit(function() {
        return element.submiter();
    });
}

