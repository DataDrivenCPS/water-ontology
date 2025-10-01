model 

"""
:t1_temp a s223:QuantifiableObservableProperty ;
    s223:hasQuantityKind qudt:Temperature ;
    s223:hasUnit unit:DEG_F ;
.
"""

"""
:t1_temp watr:hasVariableRange :t1_temp_range .
"""

"""
:t1_temp_range a s223:QuantifiableProperty ;
    s223:hasValue 0, 100 ;
.
"""

"""
:t1_temp watr:hasProcessedData :t1_temp_mean .
"""

"""
:t1_temp_mean s223:hasAspect watr:Aggregate-Mean ;
    watr:hasTemporalResolution [
        a s223:QuantifiableProperty
        s223:hasUnit qudt:HR ;
        s223:hasValue 1 ;
    ].
"""

"""
:t1_temp watr:hasDropRate [
    a s223:QuantifiableProperty ;
    s223:hasValue 10 ;
    s223:hasUnit unit:NUM-PER-HR ;
].
"""

"""
:t1_temp watr:hasProcessedData [
    a s223:QuantifiableProperty ;
    s223:hasAspect watr:Interpolation-Linear ;
        s223:hasExternalReference :t1_temp_1min ;
        watr:hasTemporalResolution [
            a s223:QuantifiableProperty
            s223:hasUnit qudt:MIN ;
            s223:hasValue 1;
        ];
    ];
.
"""