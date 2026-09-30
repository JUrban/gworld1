Read("scripts/n5_general_malcev_input.g");
Read("scripts/n5_class2_json.g");
Read("scripts/n5_general_support_fixtures.g");
N5ExportSupport:=function()
    local records,f,m;
    records:=[];
    for f in N5SupportFixtures() do
        m:=N5GeneralMalcevInput(f.group);m.data.name:=f.name;
        m.data.expected_dimensions:=f.expected_dimensions;Add(records,m.data);
        Print(f.name,": Hirsch ",m.data.hirsch_length,"\n");
    od;
    N5WriteCoordinateJson("research/certificates/N5-general-support/input-v1.json",records);
    Print("PASS N5 support export: ",Length(records)," groups\n");
end;
N5ExportSupport();
QUIT;
