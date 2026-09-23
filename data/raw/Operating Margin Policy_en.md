<!-- Machine-Extracted & Translated from Operating Margin Policy.pdf | Power System Knowledge Base -->

<!-- PAGE 1 -->

# TRANSMISSION SYSTEM OPERATOR OF CYPRUS

> [Technical Diagram Architecture Note: Logo of TSOC - Transmission System Operator of Cyprus]

# OPERATING MARGIN POLICY

**Version 1.0.0**

<!-- PAGE 2 -->

# Table of Contents

**1 Introduction** ................................................................................................................................................ 2

**2 Frequency Control** .............................................................................................................................. 2  
&nbsp;&nbsp;&nbsp;&nbsp;**2.1 Definition of Frequency Control Parameters** ......................................................................... 2

**3 System Operation and Activation of Reserves** ....................................................................... 4  
&nbsp;&nbsp;&nbsp;&nbsp;**3.1 Normal System Operation** ............................................................................................... 4  
&nbsp;&nbsp;&nbsp;&nbsp;**3.2 Operation Following Disturbances** ................................................................................................ 5  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.1 Inertial Response** ....................................................................................................... 5  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.2 Fast Regulation and Frequency Containment** ........................................................................ 5  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.3 Frequency Restoration** .................................................................................................... 7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.4 Replacement of Reserves** ..................................................................................................... 7

**4 Technical Specifications of Reserves** ..................................................................................................... 7  
&nbsp;&nbsp;&nbsp;&nbsp;**4.1 Fast Frequency Response Reserve (FFR)** ................................................................................ 7  
&nbsp;&nbsp;&nbsp;&nbsp;**4.2 Frequency Containment Reserve (FCR)** ................................................................................... 8  
&nbsp;&nbsp;&nbsp;&nbsp;**4.3 Frequency Restoration Reserve (FRR)** ............................................................................. 8  
&nbsp;&nbsp;&nbsp;&nbsp;**4.4 Replacement Reserve (RR)** ................................................................................................... 9

**5 Determination of Required Reserve Quantities** ............................................................................ 9  
&nbsp;&nbsp;&nbsp;&nbsp;**5.1.1 Fast Frequency Response Reserve and Frequency Containment Reserve** .................... 9  
&nbsp;&nbsp;&nbsp;&nbsp;**5.1.2 Frequency Restoration Reserve** ............................................................................ 13  
&nbsp;&nbsp;&nbsp;&nbsp;**5.1.3 Replacement Reserve** .................................................................................................... 14  
&nbsp;&nbsp;&nbsp;&nbsp;**5.2 Other Requirements** ...................................................................................................................... 14

**6 Current Status** .......................................................................................................................... 14  
&nbsp;&nbsp;&nbsp;&nbsp;**6.1 Upward Spinning Reserve** ................................................................................................ 15  
&nbsp;&nbsp;&nbsp;&nbsp;**6.2 Downward Spinning Reserve** .............................................................................................. 15  
&nbsp;&nbsp;&nbsp;&nbsp;**6.3 Replacement Reserve** ........................................................................................................ 15

<!-- PAGE 3 -->

# 1 Introduction

This "Operational Reserve Policy" specifies the requirements of TSOC regarding the Operational Reserve Margin, as deemed necessary to ensure the operation of the Power System of Cyprus. The provisions of this Policy will be revised whenever deemed necessary by TSOC, based on updated data arising in the Power System, study results, etc.

According to the Transmission Rules, Operational Reserve Margin is defined as the available amount of Active Power for operating reserve, after covering the expected Demand of the Power System. It includes Operating Reserve (which consists of Fast Frequency Response (FFR), Frequency Containment Reserve (FCR), and Frequency Restoration Reserve (automatic and manual, aFRR and mFRR)), Replacement Reserve (RR), and Contingency Reserve.

Contingency Reserve is not included in the present edition of the Operational Reserve Policy.

The management of the Operational Reserve Margin is carried out by TSOC in such a way as to achieve adequate Frequency Control.

# 2 Frequency Control

The objective of the frequency control process is to maintain System frequency within the predefined normal operating range or, in the event of a deviation, its recovery and restoration within a specified time frame.

Power balance disturbances and, consequently, frequency deviations outside the normal operating range can be caused by various factors. The most significant of these are the following:

1) Loss of generation and/or demand
2) Continuous stochastic variation of demand and RES generation
3) Deviation in demand forecast
4) Deviation in RES generation forecast

The occurrence of such events leads to an imbalance between generation and demand which must be restored. For this purpose, TSOC must ensure in advance sufficient quantities of power reserves so as to be able to restore the power balance within predefined time frames.

## 2.1 Determination of Frequency Control Parameters

The frequency control process is characterized by certain key parameters, the values of which are taken into account during the dimensioning of reserve requirements and the specification of technical requirements for the various reserve types. These parameters and the corresponding values applicable to the Power System of Cyprus are presented in Table 1 below.

<!-- PAGE 4 -->

### Table 1: Frequency Control Parameters

| Parameter | Value |
|---|---|
| Nominal Frequency | 50 Hz |
| Normal Operation Range | 49.8 – 50.2 Hz |
| Frequency Recovery Range<br>(Maximum Steady-State Deviation) | 49.5 – 50.5 Hz<br>(± 500 mHz) |
| Frequency Recovery Time | 20 sec |
| Intermediate Frequency Restoration Time | ~1.5 - 2 minutes |
| Frequency Restoration Range | 49.8 – 50.2 Hz |
| Frequency Restoration and Reserve Replacement Time | 25 minutes |
| Maximum Instantaneous Frequency Deviation (Frequency Nadir only) | Based on Table 4 |

"Nominal Frequency" and "Normal Operation Range" are specified in the Transmission Rules.

"Frequency Recovery Range" is defined as the range within which the frequency must return following a disturbance, within a time frame shorter than the "frequency recovery time".

In the event that the frequency remains outside the restoration range for a duration approaching the "intermediate frequency restoration time", measures may be implemented to restore it as quickly as possible, such as manual load shedding, taking into account prevailing conditions and the operational status of the units.

"Frequency restoration and reserve replacement time" is the time frame within which, following a disturbance, the frequency must return within the "frequency restoration range" (which coincides with the normal operation range) and the necessary reserves must become available so that any shed load can be reconnected.

Regarding the recovery range and restoration range, it is noted that in the Continental Europe Synchronous Area, only a restoration range is defined. However, this approach is not selected for the small and isolated system of Cyprus, as in such a case, large amounts of reserve would be required, leading to uneconomic System operation and potentially giving rise to problems such as frequency over-correction. Therefore, the approach followed in the United Kingdom and Ireland systems has been adopted, according to which, after a disturbance, the frequency must return within the recovery range as an intermediate stage prior to its full restoration.

Regarding the Maximum Instantaneous Frequency Deviation (Frequency Nadir), it is primarily determined by the extent of activation of the Automatic Under-Frequency Load Shedding (UFLS) Scheme, which is taken into account as part of the fast control and frequency containment procedure (see Table 4).

<!-- PAGE 5 -->

# 3 System Operation and Reserve Activation

The operating state of the System can be distinguished into two main categories:

i. Normal operation, during which System power generation and demand have been forecast with relative accuracy, and reserves are called upon to handle small deviations from the forecast generation/demand values. For this purpose, the automatic and manual frequency restoration reserves (aFRR and mFRR) are activated, whereas the Frequency Containment Reserve (FCR) is not activated and remains available (or is activated to a minor extent).

ii. Post-disturbance operation, during which unforeseen and sharp variations occur in the power balance. In such cases, Fast Frequency Response (FFR) reserves and FCR are initially activated, as well as potentially the Under-Frequency Load Shedding (UFLS) scheme, followed subsequently by the activation of aFRR and mFRR, and finally the Replacement Reserve (RR).

## 3.1 Normal System Operation

Within the framework of Generation Scheduling, TSOC prepares a unit commitment schedule and an indicative dispatch schedule for Balancing Service Providers (BSPs) (generation units, storage facilities, etc.), based on forecast demand and RES generation.

In real time, however, deviations from this schedule arise due to forecast errors in demand and RES generation, as well as unforeseen continuous variations in load and RES output. These deviations are balanced through the utilization of Automatic and Manual Frequency Restoration Reserves. Rapid and random variations in demand and RES generation are balanced through the activation of aFRR reserves, whereas adjustment to large-magnitude and long-duration deviations is achieved through the combined activation of aFRR and mFRR reserves.

### Automatic Frequency Restoration Reserve (aFRR)

The activation of aFRR is achieved through the Automatic Generation Control (AGC) system. The Automatic Generation Control (AGC) process centrally calculates the generation change required to correct the residual frequency error. Subsequently, the calculated generation change requirement is appropriately allocated to the System's operational Balancing Service Providers (BSPs) that are under AGC control, and their generation is adjusted accordingly via control signals sent by this system.

Currently, an operational AGC system does not exist in the Power System of Cyprus, and therefore this process is executed manually based on the description in Section 4.3.

### Manual Frequency Restoration Reserve (mFRR)

The activation of mFRR is carried out via appropriate dispatch instructions issued within the framework of the Real-Time Balancing Market or through directives issued by the National Control Center (NCC).

<!-- PAGE 6 -->

### 3.2 Operation Following Disturbances

Following the occurrence of a disturbance in the System, an immediate deviation in the power balance is caused, disturbing the System frequency. Therefore, the procedures described below are activated to restore the System to normal operation state.

#### 3.2.1 Inertial Response

The first stage of System response following the occurrence of a power balance deviation aims to limit the rate of change of frequency (RoCoF) and is characterized by the immediate physical reaction of synchronous generators via their inertial response, as well as the corresponding response of power electronic converters capable of providing synthetic inertia.

Specifically, regarding synchronous generators, the kinetic energy stored in their rotating masses reacts instantaneously in opposition (inertially) to the imbalance. Power electronic converters correspondingly increase power injection into (or reduce power absorption from) the grid in a manner that emulates the behavior of synchronous generators.

Requirements regarding inertial response are not included within the scope of this document.

#### 3.2.2 Fast Regulation and Frequency Containment

The next stage of System response following a disturbance concerns frequency containment and stabilization. This specific stage can be divided into two timeframes, with the first concerning fast regulation through the provision of Fast Frequency Response (FFR) and the second concerning frequency containment through the provision of Frequency Containment Reserve (FCR).

Within the framework of fast regulation (provision of FFR), Power Generating Modules (PGMs) possessing the relevant capability (typically storage facilities) alter their power output according to the relevant requirements, within a timeframe preceding the activation of FCR.

Subsequently, generator speed governors react to the change in System frequency and adjust generator production appropriately until System frequency reaches equilibrium, while a corresponding contribution is also provided by units connected via power electronics that possess the relevant capability (provision of FCR).

The frequency equilibrium point at the end of this stage (steady-state deviation) must lie within the "Frequency Recovery Range" and must be achieved within a timeframe not exceeding the "Frequency Recovery Time", as specified in Paragraph 2.1. This deviation is corrected in the subsequent stage of the process with the contribution of Frequency Restoration Reserve.

Furthermore, in cases where the deviation involves a frequency drop, a contribution is also obtained from the potential operation of the Under-Frequency Load Shedding (UFLS) Scheme.

##### Under-Frequency Load Shedding (UFLS) Scheme

The Under-Frequency Load Shedding Scheme involves the automatic disconnection of Medium Voltage (MV) feeders from the distribution network in the event that the frequency drop following a disturbance exceeds specific limits.

The implementation of UFLS is based on 15 distinct stages, with each stage being activated based on measurable parameters of frequency and its rate of change ($df/dt$), as presented in Table 2 below.

<!-- PAGE 7 -->

### Table 2: Under-Frequency Load Shedding Scheme (UFLS)

| Load Shedding Stage | Shedding Frequency (Hz) | Shedding Delay (sec) | Required Shedding Percentage (%) |
|---|---|---|---|
| 1 | 49.0 | 0.2 | 4% |
| 2 | 48.9 | 0.2 | 4% |
| 3 | 48.8 | 0.2 | 3% |
| 4 | 48.7 | 0.2 | 8% |
| 5 | 48.6 | 0.2 | 4% |
| 6 | 48.5 | 0.2 | 4% |
| 7 | 48.4 | 0.2 | 4% |
| 8 | 48.3 | 0.2 | 1% |
| 9 | 48.2 | 0.35 | 7% |
| 10 | 48.1 | 0.35 | 6% |
| 11 | 48.0 | 0.35 | 5% |
| 12 | 47.75 | 0.35 | 9% |
| 13 | 47.5 | 0.35 | 9% |
| 14 | 49.5* | * | * |
| 15 | 49.9** | ** | ** |

\* Stage 14 consists of eight distinct disconnection groups, which are activated with a time delay ranging from 25 to 65 seconds, provided that the frequency remains within the range of 49 Hz – 49.5 Hz.

\*\* Stage 15 is activated when the rate of change of frequency (df/dt) exceeds 1 Hz/sec, with the frequency drop from 49.9 Hz occurring within 0.3 seconds.

The activation of the UFLS constitutes a critical mechanism for maintaining the stability of the power system, preventing the propagation of disturbances and total system collapse.

<!-- PAGE 8 -->

### 3.2.3 Frequency Restoration

The frequency restoration stage aims to correct the steady-state frequency deviation. Furthermore, during the frequency restoration stage, the reserves that were activated are restored, so that the capability of units to re-participate in the frequency containment process is restored.

The frequency restoration process follows the process of fast regulation and frequency containment, and is achieved through two distinct mechanisms:

* automatically, via the Automatic Generation Control (AGC) system, and
* manually, through the issuance of dispatch instructions within the framework of the Real-Time Balancing Market or following instructions from the NCC (National Control Center).

Additionally, in cases where the deviation involves a frequency drop, automatic (via UFLS) and/or manual load shedding contributes to the frequency restoration process.

### 3.2.4 Replacement Reserve

The final stage of the frequency control process concerns the replacement of power reserves that were activated during the frequency restoration process, so that they become available again for activation and for the reconnection of any shed load.

---

# 4 Technical Specifications for Reserves

## 4.1 Fast Frequency Response Reserve (FFR)

The operation and mode of provision of FFR is described by the following Diagram 1.

> [Technical Diagram Architecture Note: Diagram 1: FFR Specifications]
> *Diagram Parameters:*
> - **Activation instant**: The point in time at which the frequency event triggers the response.
> - **Activation time**: Time required from trigger to reach full output response.
> - **Support duration**: Duration for which the active power support is sustained.
> - **Deactivation time**: Time required for output reduction following support.
> - **Buffer time before recovery**: Idle period before energy recovery phase starts.
> - **Recovery time**: Period over which energy balance/state-of-charge is recovered.
> - **Recovery**: Energy recovery trajectory/period back to initial baseline.

**Diagram 1: FFR Specifications**

In Table 3 below, indicative values regarding the parameters shown in Diagram 1 are provided. TSOC may divide the total required quantity of FFR into sub-quantities with different values for the parameters of Table 3, aiming to maximize the benefit from the contribution of FFR.

<!-- PAGE 9 -->

### Table 3: Indicative parameter values for FFR provision

| Parameter | Value |
|---|---|
| Activation level (Hz) | 49.7 |
| Maximum activation time (s) | 0.8 |
| Support duration (s) | 30 |
| Deactivation time (s) | 20 |
| Buffer time before recovery (s) | 40 |
| Recovery time (min) | ~13.5 |

---

### 4.2 Frequency Containment Reserve (FCR)

FCR is provided by units operating in Frequency Sensitivity Mode (FSM).

The application of deadbands to frequency variations (beyond the inherent deadband of governors/controllers) is performed only upon instructions or following agreement with TSOC.

The activation of Frequency Containment Reserve is not artificially delayed and begins to be provided as soon as possible after a Frequency deviation from the Target Frequency.

Following a frequency change, the unit must activate at least 45% of its theoretical FCR provision capability within 5 seconds and 90% within 20 seconds, which must be sustained for 25 minutes.

The theoretical FCR provision capability is derived based on the unit's governor droop value. This value is set to 4%, unless agreed otherwise with TSOC.

The FCR provision capability declared in the registered operating characteristics of a unit is the quantity provided for a step change in frequency of 0.5 Hz.

---

### 4.3 Frequency Restoration Reserve (FRR)

aFRR must become fully available within 5 minutes from its activation, and mFRR within 15 minutes.

The required quantity of aFRR and mFRR must be capable of remaining available for a period of 30 minutes.

It is noted that currently, in the Power System of Cyprus, an AGC system is not in operation; therefore, the provision of aFRR will be performed via manual interventions on Generating Units, simulating the operation of automated control. As previously mentioned, under normal operating conditions, the goal of activating aFRR is to balance fast and random variations in demand. Consequently, the operators of Generating Units tasked with providing this specific service, and thereby with the regulation of

<!-- PAGE 10 -->

...frequency, shall continuously monitor System frequency and adjust their Unit generation accordingly to achieve the target desired frequency. Correspondingly, under disturbance conditions, they shall adjust their Unit generation as soon as possible after the occurrence of the Event with the aim of restoring the frequency.

### 4.4 Replacement Reserve (RR)

The Replacement Reserve must become fully available within 25 minutes of its activation.

---

# 5 Determination of Required Reserve Quantities

## 5.1.1 Fast Frequency Response Reserve and Frequency Containment Reserve

As stated in Section 3, the process of fast regulation and containment of frequency concerns operation following disturbances. During this process, available FFR and FCR quantities are activated, as well as potentially the Under-Frequency Load Shedding (UFLS) scheme (in cases of frequency drop below 49.0 Hz).

### Upward Reserves

The available quantities of FCR and FFR must be such that, following the occurrence of the Reference Incident, the frequency recovers within the "Frequency Recovery Range" in a time not exceeding the "Frequency Recovery Time", ensuring that the Frequency Nadir will not exceed the "Maximum Instantaneous Frequency Deviation".

The Reference Incident regarding loss of generation in the Power System of Cyprus is defined as the loss of 120 MW (corresponding to the loss of the largest unit at full load and/or the largest generation loss from RES considered during Transmission Network design).

The determination of the necessary quantities to achieve the above results from dynamic analyses simulating the response of the System.

An important parameter for determining the necessary reserve quantities, in cases of frequency drop, is the operation of the Under-Frequency Load Shedding Scheme, and specifically the scheme activation stages that are considered as part of the fast frequency regulation and containment process.

Since UFLS involves disconnecting a specific percentage of load at each stage, different scenarios in relation to the total System load must be considered.

It is also noted that total load affects System response (to a small degree) through load self-regulation.

The number of UFLS stages that will operate in each case is affected by the inertial response of the units remaining after the disturbance and the activation of FFR, as these influence the rate of change of frequency (RoCoF) and the Frequency Nadir following the disturbance.

<!-- PAGE 11 -->

System inertia can take various values, as it depends on the units synchronized to the System in each case (the minimum acceptable amount is that which ensures that the Rate of Change of Frequency in the event of a disturbance will not exceed 1 Hz/sec, in accordance with the provisions of the Market Rules).

Additionally, the required amount of FCR varies depending on the activated UFLS stages and the total System load.

Taking the above into account, simulations of a large number of scenarios with different levels of inertia and available FFR have been carried out, the results of which are summarized in Table 4.

Table 4 presents the required amount of FCR for different values of FFR and number of activated UFLS stages, for low, medium, and high load conditions, as well as the percentage of scenarios (out of the total number of studied scenarios) where the activation of 0, 1, 2, 3, or more UFLS stages was observed.

For example, with an available FFR capacity equal to 40 MW, in 38.87% of the scenarios, only the first two UFLS stages were activated. Therefore, the required amount of FCR was 95 MW, 78 MW, and 27 MW for low, medium, and high load conditions, respectively.

From the values in Table 4, based on the availability of FFR and FCR providers as well as the UFLS activation stages taken into account as part of the fast frequency regulation and containment process, the applicable combination of FFR and FCR requirements will be determined.

#### Table 4: Simulation results for a 120 MW generation loss incident

| Available FFR Service (MW) | U/F Activation Stage (nadir) | Percentage of Scenarios with Activation of Corresponding U/F Stage | Required FCR Quantity: Low Load (MW) | Required FCR Quantity: Medium Load (MW) | Required FCR Quantity: High Load (MW) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **100** | 0 (f > 49 Hz) | 100.00% | 119 | 118 | 115 |
| **80** | 2 (48.9 Hz) | 1.13% | 95 | 78 | 27 |
| | 1 (49.0 Hz) | 8.30% | 107 | 98 | 71 |
| | 0 (f > 49 Hz) | 90.57% | 119 | 118 | 115 |
| **60** | 3 (48.8 Hz) | 0.75% | 86 | 63 | 0 |
| | 2 (48.9 Hz) | 12.45% | 95 | 78 | 27 |
| | 1 (49.0 Hz) | 40.00% | 107 | 98 | 71 |
| | 0 (f > 49 Hz) | 46.80% | 119 | 118 | 115 |

<!-- PAGE 12 -->

| Parameter | Frequency / UFLS Stage | Percentage | Option 1 | Option 2 | Option 3 |
|---|---|---|---|---|---|
| **40** | $\ge 4 \ (f \le 48.7\text{ Hz})$ | 7.92% | 62 | 23 | 0 |
| | 3 (48.8 Hz) | 9.81% | 86 | 63 | 0 |
| | 2 (48.9 Hz) | 38.87% | 95 | 78 | 27 |
| | 1 (49.0 Hz) | 33.21% | 107 | 98 | 71 |
| | 0 ($f > 49\text{ Hz}$) | 10.19% | 119 | 118 | 115 |
| **20** | $\ge 4 \ (f \le 48.7\text{ Hz})$ | 32.72% | 62 | 23 | 0 |
| | 3 (48.8 Hz) | 19.73% | 86 | 63 | 0 |
| | 2 (48.9 Hz) | 35.85% | 95 | 78 | 27 |
| | 1 (49.0 Hz) | 11.7% | 107 | 98 | 71 |
| | 0 ($f > 49\text{ Hz}$) | 0% | 119 | 118 | 115 |
| **0** | $\ge 4 \ (f \le 48.7\text{ Hz})$ | 47.17% | 62 | 23 | 0 |
| | 3 (48.8 Hz) | 28.30% | 86 | 63 | 0 |
| | 2 (48.9 Hz) | 17.36% | 95 | 78 | 27 |
| | 1 (49.0 Hz) | 7.17% | 107 | 98 | 71 |
| | 0 ($f > 49\text{ Hz}$) | 0% | 119 | 118 | 115 |

---

### Downward Reserves

Downward reserves aim to cover deviations resulting from disturbances caused either by loss of load or by a sudden increase in RES generation.

As a Reference Incident for the purpose of downward reserve sizing, a loss of load of the order of 60 MW is defined (based on historical data).

The requirements for downward reserves are calculated based on the frequency regulation coefficient ($\lambda = \Delta P_{\max}/\Delta f_{\max}$).

During the sizing of requirements, the automatic reduction of RES generation in cases of frequency deviation beyond specific thresholds is taken into account, based on the settings applied to power inverters. Therefore, sizing is performed for different levels of PV or Wind generation.

Additionally, load self-regulation is taken into account, so sizing is performed for different levels of total system load.

It is noted that currently no requirements are defined for downward FFR.

Taking the above into account, Table 5 is established, presenting the downward FCR requirements for different conditions of total load and PV and Wind generation.

<!-- PAGE 13 -->

### Table 5: Downward FCR Requirements

| Total Load | PV Generation | Wind Generation | Required FCR Quantity (MW) |
| :--- | :--- | :--- | :---: |
| **Minimum Load** | Minimum | Minimum | 59 |
| | | Medium | 41 |
| | | Maximum | 0 |
| | Medium | Minimum | 41 |
| | | Medium | 23 |
| | | Maximum | 0 |
| | Maximum | Minimum | 11 |
| | | Medium | 0 |
| | | Maximum | 0 |
| **Medium Load** | Minimum | Minimum | 58 |
| | | Medium | 40 |
| | | Maximum | 0 |
| | Medium | Minimum | 40 |
| | | Medium | 22 |
| | | Maximum | 0 |
| | Maximum | Minimum | 10 |
| | | Medium | 0 |
| | | Maximum | 0 |
| **Maximum Load** | Minimum | Minimum | 55 |
| | | Medium | 37 |
| | | Maximum | 0 |
| | Medium | Minimum | 37 |
| | | Medium | 19 |
| | | Maximum | 0 |

<!-- PAGE 14 -->

| | Minimum | 7 |
| --- | --- | --- |
| Maximum | Average | 0 |
| | Maximum | 0 |

### Calculation of FCR Requirement

As mentioned above, the requirement for FCR depends on the level of load demand and RES generation, which vary for each hour of the day as well as from day to day.

Therefore, it is necessary to size the required FCR on a daily basis for the next day, based on the data mentioned above, so that it is taken into account within the framework of generation scheduling.

### 5.1.2 Frequency Restoration Reserve

As mentioned in Section 3, the Frequency Restoration Reserve is activated both under normal operating conditions and under disturbance conditions.

Under normal operating conditions, rapid and stochastic variations in demand and RES generation are balanced through the activation of aFRR reserves, whereas adaptation to large-scale and long-duration imbalances is achieved through the combined activation of aFRR and mFRR reserves.

In cases of disturbances, aFRR and mFRR contribute to frequency restoration after the frequency has returned within the recovery range.

Based on its description, the sizing of FRR must take into account both the requirements for covering imbalances under normal operating conditions and the requirements for restoring frequency following a disturbance.

In the small and isolated System of Cyprus, where inertia is low and RES penetration is significantly high, the resulting requirements for covering imbalances under normal operating conditions are particularly high relative to the size of the System.

In parallel, potential generation loss incidents include losses representing a large percentage of generation.

As a result, the requirements resulting from the various methodologies used to cover both conditions are deemed unrealistic in terms of the capability to secure them under current conditions.

Consequently, an approach has been selected whereby the sizing of FRR will take into account only the requirements for covering demands under normal operating conditions.

In cases of disturbances, frequency restoration will be achieved through the activation of the available FRR volume after the disturbance (after covering normal operation imbalances) in combination with manual load shedding by the NCC, if required, in cases of generation deficit, or RES generation curtailment in cases of generation surplus (either automatically as mentioned in Section 5.1.1 or manually).

Due to the fact that FRR requirements under normal operating conditions are primarily determined by the continuous stochastic variation of demand and RES generation, as well as imbalances in

---
*Page 13*

<!-- PAGE 15 -->

... demand load forecast and RES generation forecast; these differ for every hour of the day and from day to day.

Therefore, it is necessary to dimension the required FRR daily for the next day, in order to be taken into account within the framework of generation scheduling.

Towards this direction, TSOC has developed software in collaboration with CUT (Cyprus University of Technology) to calculate the requirements (discretely for aFRR and mFRR) based on probabilistic methods.

Finally, it is noted that to cover deviations that may arise from RES generation forecasting error in the downward direction, the capability to reduce RES generation (curtailment) is utilized, since maintaining FRR quantities to cover such deviations would lead to greater curtailment requirements and uneconomic system operation.

### 5.1.3 Replacement Reserve

Replacement Reserve is activated primarily for the purpose of restoring reserves that were activated due to a disturbance and reconnecting loads that were disconnected automatically (due to UFLS activation) or manually.

The relevant requirements are currently specified for the upward direction only.

The minimum requirement is defined as the largest negative power imbalance that can be observed from the loss of a single conventional unit in the Cyprus EPS.

### 5.2 Other Requirements

To ensure the availability of each type of reserve in the event of a generating unit loss, the maximum Percentage of Available Reserve Power that a Generating Unit can provide for each reserve type is specified as follows:

i. FCR = 35%
ii. aFRR = 35%
iii. mFRR = 50%
iv. RR = 25%

These percentages are established so that the remaining reserve following an incident is distributed among multiple units of the System.

## 6 Current Situation

Due to the specific conditions of the Cyprus Electrical Power System, namely the fact that it constitutes a small and isolated system with particularly high RES penetration and units of large nominal capacity relative to the size of the System, the required reserves to ensure its smooth operation turn out to be quite high.

Full implementation of the Operating Margin Policy presupposes the availability of a sufficient number of providers so that securing the required quantities of reserves in an economically acceptable manner is feasible—a condition that currently does not hold in the Cyprus Electrical Power System.

Consequently, TSOC is compelled to maintain smaller reserve quantities, resorting in parallel to supplementary measures, such as load shedding or utilizing fast-start generators to cover deviations under normal operating conditions.

The reserve quantities currently maintained are recorded in the following paragraphs.

<!-- PAGE 16 -->

### 6.1 Upward Spinning Reserve

An initial requirement in the range of 40–60 MW is maintained (and for short periods, during peak hours, 30 MW), of which 30–50 MW constitute FCR (Frequency Containment Reserve).

Additionally, an extra amount of upward spinning reserve is maintained for the purpose of covering RES forecasting errors as follows (the corresponding quantities in the downward direction are provided via RES curtailment):

* **Reserve for wind power forecasting error**
  * An additional spinning reserve approximately equal to 50% of the forecasted wind generation is maintained.
  * It is defined in discrete steps/tranches relative to the forecasted generation.

* **Reserve for photovoltaic generation forecasting deviation**
  * An additional spinning reserve between 0–25% of the forecasted PV generation is maintained.
  * It is determined based on available meteorological data in combination with seasonality and expected weather conditions regarding cloud cover, dust, etc.

It is understood that the above quantities are adjusted appropriately based on the expected curtailment.

---

### 6.2 Downward Spinning Reserve

A requirement in the order of 25 MW is maintained to cover fluctuations in RES generation and potential loss of demand/load. This value increases during periods of high RES generation and high RES variability up to 35–40 MW, whereas it decreases during periods of low RES variability down to 15–20 MW.

---

### 6.3 Replacement Reserve

Maintained in the upward direction only, in a quantity equal to the available nominal capacity of the largest unit of the System.

