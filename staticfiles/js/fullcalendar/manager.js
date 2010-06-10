function CalendarManager(full_calendar) {
    this.full_calendar = full_calendar;
    this.events_sources = [];
    this.lolilol = "lolilol";

    this.EventSource = function(type, url, id) {
        this.type = type;
        this.id = id;
        this.url = url;
        this.displayed = false;

        this.Event = function(fc_event) {
            this.fc_event = fc_event;
        };
        this.events = [];
        this.add_event = function (fc_event) {
            this.events.push(fc_event);
        };
    }

    this.add_event_source = function (type, url, id ) {
        name = type+id;
        this.events_sources[name] = (new this.EventSource(type, url,  id));
    };

    this.purge_event_source = function (name) {
        for(i in this.events_sources[name].events)
        {
            //Purge the events we added
            to_remove = this.events_sources[name].events[i];
            this.full_calendar.fullCalendar('removeEvents', to_remove);
        }
        this.events_sources[name].events = [];
    };

    this.display_event_source = function(name) {
        if(this.events_sources[name].displayed == false)
        {
            this.full_calendar.fullCalendar('addEventSource',
            this.events_sources[name].url);
            this.events_sources[name].displayed = true;
        }
    };

    this.hide_event_source = function(name) {
        this.full_calendar.fullCalendar('removeEventSource',
        this.events_sources[name].url);
        this.purge_event_source(name);
        this.events_sources[name].displayed = false;
    };

    this.add_event = function(source_name, fc_event) {
        this.events_sources[source_name].add_event(fc_event);
        this.full_calendar.fullCalendar('renderEvent', fc_event);
    };

}

function CalendarCheckbox(element, fc_manager, url_base)
{
    element.data("fc_mgr", fc_manager);
    element.data("src_type", element.val());
    fc_manager.add_event_source(element.val(), url_base + element.val(), "");
    element.check_function = function() {
        if(this[0].checked)
            $(this).data("fc_mgr").display_event_source($(this)
                                                .data("src_type"))
        else
            $(this).data("fc_mgr").hide_event_source($(this)
                                                .data("src_type"))
    };

    element.click(function() {element.check_function()});
    element.check_function();
}



function CalendarSelector(element, source_type, fc_manager, url_base)
{
    this.element = element;
    this.source_type = source_type;
    this.fc_manager = fc_manager;
    this.ids = [];

    url_base = url_base + source_type + "/";
    
    children = element.children("option").map(function(u, elem) {
        return elem;
        }).get();
    
    for(i in children)
    {
        fc_manager.add_event_source(source_type, url_base + children[i].value,
                                                            children[i].value);
        this.ids.push(children[i].value);
    }
 
    element.data("ids", this.ids);
    element.data("fc_mgr", fc_manager);
    element.data("src_type", source_type);
    element.check_function = function () {
        var ids = $(this).data("ids");
        for(i in ids) {
            mval = $(this).val();
            if($.inArray(ids[i], mval) >= 0)
            {
                $(this).data("fc_mgr").display_event_source($(this)
                                                    .data("src_type")+
                                                    $(this).data("ids")[i])
            }
            else
            {
                $(this).data("fc_mgr").hide_event_source($(this)
                                                    .data("src_type")+
                                                    $(this).data("ids")[i])
            }
        }

    };

    element.change(function() {element.check_function()});
    element.check_function();
}


function CalendarSubmiter(element, fc_manager, source_name, callback)
{
    element.data("url", fc_manager.events_sources[source_name]);
    element.data("fc_mgr", fc_manager);
    element.submiter = function () {
        url = $(this).data("url");
        fc_mgr = $(this).data("fc_mgr");
        $.post(url, $(this).serialize(),
            function(data) {
               fc_mgr.add_event(data, source.name), "json"});
        return false;
        }
    element.submit(function() {
        return element.submiter();
    });
}

