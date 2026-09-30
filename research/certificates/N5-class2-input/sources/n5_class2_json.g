# Small data-only JSON writer: integer arrays, records, nonempty strings,
# booleans. No GAP objects or executable input are serialized.
N5CoordinateJson:=function(x)
    local keys;
    if IsBool(x) and x<>fail then return String(x);fi;
    if IsInt(x) then return String(x);fi;
    if IsString(x) and Length(x)>0 then
        return Concatenation("\"",ReplacedString(ReplacedString(x,"\\","\\\\"),"\"","\\\""),"\"");
    fi;
    if IsList(x) then return Concatenation("[",JoinStringsWithSeparator(List(x,N5CoordinateJson),","),"]");fi;
    if IsRecord(x) then
        keys:=ShallowCopy(RecNames(x));Sort(keys);
        return Concatenation("{",JoinStringsWithSeparator(List(keys,k->
            Concatenation(N5CoordinateJson(k),":",N5CoordinateJson(x.(k)))),","),"}");
    fi;
    Error("unsupported coordinate JSON value");
end;
N5WriteCoordinateJson:=function(path,data)
    local stream;
    stream:=OutputTextFile(path,false);SetPrintFormattingStatus(stream,false);
    PrintTo(stream,N5CoordinateJson(data),"\n");CloseStream(stream);
end;
