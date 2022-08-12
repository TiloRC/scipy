# DO NOT EDIT THIS FILE!
# This file was generated by the R script
#     generate_fisher_exact_results_from_r.R
# The script was run with R version 3.6.2 (2019-12-12) at 2020-11-09 06:16:09


from collections import namedtuple
import numpy as np


Inf = np.inf

Parameters = namedtuple('Parameters',
                        ['table', 'confidence_level', 'alternative'])
RResults = namedtuple('RResults',
                      ['pvalue', 'conditional_odds_ratio',
                       'conditional_odds_ratio_ci'])
data = [
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.1300759363430016,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0.04035202926536294,
                                         2.662846672960251))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.02301413756522116,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0.004668988338943325,
                                         0.895792956493601))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.1973244147157191,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0.4153910882532168,
                                         259.2593661129417))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.09580440012477633,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0.08056337526385809,
                                         1.22704788545557))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.2697004098849359,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0.1176691231650079,
                                         1.787463657995973))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.1973244147157192,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0.003857141267422399,
                                         2.407369893767229))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.06126482213438735,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         1.451643573543705))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.04761904761904762,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(1.024822256141754,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         39.00054996869288))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.04761904761904761,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(1.024822256141754,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         39.00054996869287))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=2.005657880389071e-122,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(349.2595113327733,
                                         3630.382605689872))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=5.728437460831947e-44,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(152.4166024390096,
                                         1425.700792178893))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.95,
                alternative='two.sided'),
     RResults(pvalue=0.574111858126088,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0.8520462587912048,
                                         1.340148950273938))),
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.1300759363430016,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0.02502345007115455,
                                         6.304424772117853))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.02301413756522116,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0.001923034001462487,
                                         1.53670836950172))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.1973244147157191,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0.2397970951413721,
                                         1291.342011095509))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.09580440012477633,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0.05127576113762925,
                                         1.717176678806983))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.2697004098849359,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0.07498546954483619,
                                         2.506969905199901))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.1973244147157192,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0.0007743881879531337,
                                         4.170192301163831))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.06126482213438735,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         2.642491011905582))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.04761904761904762,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0.496935393325443,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         198.019801980198))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.04761904761904761,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0.496935393325443,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         198.019801980198))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=2.005657880389071e-122,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(270.0334165523604,
                                         5461.333333326708))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=5.728437460831947e-44,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(116.7944750275836,
                                         1931.995993191814))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.99,
                alternative='two.sided'),
     RResults(pvalue=0.574111858126088,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0.7949398282935892,
                                         1.436229679394333))),
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.1300759363430016,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0,
                                         1.797867027270803))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.0185217259520665,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0,
                                         0.6785254803404526))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.9782608695652173,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0,
                                         127.8497388102893))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.05625775074399956,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0,
                                         1.032332939718425))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.1808979350599346,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0,
                                         1.502407513296985))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.1652173913043479,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0,
                                         1.820421051562392))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.0565217391304348,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         1.06224603077045))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.5,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         19.00192394479939))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.4999999999999999,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         19.00192394479939))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(0,
                                         3045.460216525746))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(0,
                                         1186.440170942579))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.95,
                alternative='less'),
     RResults(pvalue=0.7416227010368963,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0,
                                         1.293551891610822))),
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.1300759363430016,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0,
                                         4.375946050832565))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.0185217259520665,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0,
                                         1.235282118191202))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.9782608695652173,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0,
                                         657.2063583945989))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.05625775074399956,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0,
                                         1.498867660683128))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.1808979350599346,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0,
                                         2.186159386716762))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.1652173913043479,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0,
                                         3.335351451901569))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.0565217391304348,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         2.075407697450433))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.5,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         99.00009507969122))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.4999999999999999,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         99.00009507969123))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(0,
                                         4503.078257659934))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=1,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(0,
                                         1811.766127544222))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.99,
                alternative='less'),
     RResults(pvalue=0.7416227010368963,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0,
                                         1.396522811516685))),
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.979790445314723,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0.05119649909830196,
                                         Inf))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.9990149169715733,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0.007163749169069961,
                                         Inf))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.1652173913043478,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0.5493234651081089,
                                         Inf))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.9849086665340765,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0.1003538933958604,
                                         Inf))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.9330176609214881,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0.146507416280863,
                                         Inf))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.9782608695652174,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0.007821681994077808,
                                         Inf))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.02380952380952382,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(1.487678929918272,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.0238095238095238,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(1.487678929918272,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=2.005657880388915e-122,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(397.784359748113,
                                         Inf))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=5.728437460831983e-44,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(174.7148056880929,
                                         Inf))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.95,
                alternative='greater'),
     RResults(pvalue=0.2959825901308897,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0.8828406663967776,
                                         Inf))),
    (Parameters(table=[[100, 2], [1000, 5]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.979790445314723,
              conditional_odds_ratio=0.25055839934223,
              conditional_odds_ratio_ci=(0.03045407081240429,
                                         Inf))),
    (Parameters(table=[[2, 7], [8, 2]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.9990149169715733,
              conditional_odds_ratio=0.0858623513573622,
              conditional_odds_ratio_ci=(0.002768053063547901,
                                         Inf))),
    (Parameters(table=[[5, 1], [10, 10]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.1652173913043478,
              conditional_odds_ratio=4.725646047336587,
              conditional_odds_ratio_ci=(0.2998184792279909,
                                         Inf))),
    (Parameters(table=[[5, 15], [20, 20]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.9849086665340765,
              conditional_odds_ratio=0.3394396617440851,
              conditional_odds_ratio_ci=(0.06180414342643172,
                                         Inf))),
    (Parameters(table=[[5, 16], [16, 25]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.9330176609214881,
              conditional_odds_ratio=0.4937791394540491,
              conditional_odds_ratio_ci=(0.09037094010066403,
                                         Inf))),
    (Parameters(table=[[10, 5], [10, 1]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.9782608695652174,
              conditional_odds_ratio=0.2116112781158479,
              conditional_odds_ratio_ci=(0.001521592095430679,
                                         Inf))),
    (Parameters(table=[[10, 5], [10, 0]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[5, 0], [1, 4]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.02380952380952382,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0.6661157890359722,
                                         Inf))),
    (Parameters(table=[[0, 5], [1, 4]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[5, 1], [0, 4]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.0238095238095238,
              conditional_odds_ratio=Inf,
              conditional_odds_ratio_ci=(0.6661157890359725,
                                         Inf))),
    (Parameters(table=[[0, 1], [3, 2]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=1,
              conditional_odds_ratio=0,
              conditional_odds_ratio_ci=(0,
                                         Inf))),
    (Parameters(table=[[200, 7], [8, 300]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=2.005657880388915e-122,
              conditional_odds_ratio=977.7866978606228,
              conditional_odds_ratio_ci=(297.9619252357688,
                                         Inf))),
    (Parameters(table=[[28, 21], [6, 1957]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=5.728437460831983e-44,
              conditional_odds_ratio=425.2403028434684,
              conditional_odds_ratio_ci=(130.3213490295859,
                                         Inf))),
    (Parameters(table=[[190, 800], [200, 900]],
                confidence_level=0.99,
                alternative='greater'),
     RResults(pvalue=0.2959825901308897,
              conditional_odds_ratio=1.068697577856801,
              conditional_odds_ratio_ci=(0.8176272148267533,
                                         Inf))),
]