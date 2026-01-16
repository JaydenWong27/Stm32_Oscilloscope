# STM32 Digital Oscilloscope
A fully implemented oscilloscope-style data acquisition system built using an stm32 microcontroller. 
The project captures analog signals utilizing a timer-driven ADC with DMA, streaming the data over to UART.

## Features

- Timer-triggered ADC sampling
- Fixed and deterministic sample rate
- DMA-based waveform capture (no CPU polling)
- UART waveform streaming (CSV / raw format)
- Software trigger (rising edge / threshold)
- Designed and tested analog frontend with biasing
- No external display required (PC-based visualization)

## Hardware Requirements

- STM32 development board (tested on STM32 family with HAL support)
- Analog signal source:
  - Potentiometer
  - Function generator
  - DAC or PWM + RC filter
- UART interface (USB or external adapter)
- Analog frontend components:
  - Op-amp (LM358 or rail-to-rail equivalent)
  - Resistor divider network
  - Biasing network (1.65 V virtual ground)

## Software Requirements

- STM32CubeIDE
- STM32 HAL drivers
- Serial terminal (PuTTY, Tera Term, minicom, etc.)
- (Optional) Python / Excel / MATLAB for plotting

## System Overview

### ADC Configuration
- Resolution: 12-bit
- Conversion mode: External trigger
- Trigger source: Timer TRGO
- Sampling method: DMA

### Timer Configuration
- Timer used: TIM2 / TIM3
- Trigger event: Update event (TRGO)
- Sample rate: Configurable (e.g. 10 kHz)

### DMA Configuration
- Mode: Normal or circular
- Buffer size: 256 / 512 samples
- Completion interrupt enabled


