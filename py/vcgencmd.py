import subprocess

_debug = False
def set_debug(enable:bool = True):
    global _debug
    _debug = enable

def _execute_command(cmd, arg=None):
    if _debug:
        print(f'vcgencmd {cmd} {arg}')

    if arg is None:
        result = subprocess.check_output(['/opt/vc/bin/vcgencmd',cmd]).decode('utf-8')
    else:    
        result = subprocess.check_output(['/opt/vc/bin/vcgencmd',cmd, arg]).decode('utf-8')

    if _debug:
        print(result)
    
    return result


def measure_clock(src):
    result = _execute_command(f'measure_clock {src}').strip()
    return int(result[result.find('=') +1:].strip())

def measure_clock_arm():
    return measure_clock('arm')

def measure_clock_core():    
    return measure_clock('core')

def measure_clock_h264():
    return measure_clock('h264')

def measure_clock_isp():
    return measure_clock('isp')

def measure_clock_v3d():
    return measure_clock('v3d')

def measure_clock_uart():
    return measure_clock('uart')

def measure_clock_pwm():
    return measure_clock('pwm')

def measure_clock_emmc():
    return measure_clock('emmc')

def measure_clock_pixel():
    return measure_clock('pixel')

def measure_clock_vec():
    return measure_clock('vec')

def measure_clock_hdmi():
    return measure_clock('hdmi')

def measure_clock_dpi():
    return measure_clock('dpi')

def measure_volts(src):
    result = _execute_command(f'measure_volts {src}')
    return float(result[result.find('=') +1:].strip().rstrip('V'))

def measure_volts_core():
    return measure_volts('core')

def measure_volts_sdram_c():
    return measure_volts('sdram_c')

def measure_volts_sdram_i():
    return measure_volts('sdram_i')

def measure_volts_sdram_p():
    return measure_volts('sdram_p')

def measure_temp():
    result = _execute_command('measure_temp')
    return float(result[result.find('=') + 1:].strip().rstrip('\'C'))

def codec_enabled(src):
    result = _execute_command('codec_enabled {src}')
    result = result[result.find('=') + 1:].strip()
    valid = {'disabled','enabled'}
    if result not in valid:
        raise Exception(f'Unknown response: {result}')
    return result.index(result) == 1

def codec_enabled_h264():
    return codec_enabled('h264')

def codec_enabled_mpg2():
    return codec_enabled('mpg2')

def codec_enabled_mpg4():
    return codec_enabled('mpg4')

def codec_enabled_mjpg():
    return codec_enabled('mjpg')

def codec_enabled_mvc0():
    return codec_enabled('mvc0')

def codec_enabled_wvc1():
    return codec_enabled('wvc1')

def codec_enabled_wmv9():
    return codec_enabled('wmv9')

def get_mem(src):
    output = _execute_command(f'get_mem {src}')
    mem = output[output.find('=') + 1:].strip()    
    return int(mem[:-1]) * 1024 * 1024 if mem[-1] == 'M' else int(mem[:-1]) * 1024 * 1024 * 1024 if mem[-1]  == 'G' else -1

def get_mem_arm():
    return get_mem('arm')

def get_mem_gpu():
    return get_mem('gpu')

def get_config_int():
    result = _execute_command('get_config int').splitlines()
    return { i.split('=')[0] : int(i.split('=')[1], 0) for i in result }

def get_config_str():
    result = _execute_command('get_config int').splitlines()
    return { i.split('=')[0] : i.split('=')[1] for i in result }

def version():
    return _execute_command('version').splitlines()

def otp_dump():
    result = _execute_command('otp_dump').splitlines()
    return { i.split(':')[0]: i.split(':')[1] for i in result }

def display_power(src:int, enable:bool):    
    result = _execute_command(f'display_power {int(enable)} {src}').strip()
    return bool(int(result[result.find('=') +1:]))

def get_display_power():
    result = _execute_command(f'display_power').strip()
    return bool(int(result[result.find('=') +1:]))

def set_display_power_main_lcd(enable:bool):
    return display_power(0,enable)

def set_display_power_secondary_lcd(enable:bool):
    return display_power(1,enable)

def set_display_power_hdmi_0(enable:bool):
    return display_power(2,enable)

def set_display_power_hdmi_1(enable:bool):
    return display_power(7,enable)

def set_display_power_composite(enable:bool):
    return display_power(3,enable)

def get_lcd_info():
    return _execute_command('get_lcd_info')

def mem_oom():
    return _execute_command('mem_oom')

def get_camera():
    result = _execute_command('get_camera').split(' ')
    return { i.split('=')[0]: bool(int(i.split('=')[1])) for i in result }

def get_camera_supported():
    return get_camera()['supported']

def get_camera_enabled():
    return get_camera()['enabled']

def get_throttled():
    return int(_execute_command('get_throttled').strip().split('=')[1], 0)

def get_throttled_is_arm_freq_capped():
    return bool(get_throttled() & (1 >> 1))

def get_throttled_is_throttled():
    return bool(get_throttled() & (1 >> 2))

def get_throttled__is_under_voltage():
    return bool(get_throttled() & (1 >> 0))

def get_throttled_was_arm_freq_capped():
    return bool(get_throttled() & (1 >> 17))

def get_throttled_was_throttled():
    return bool(get_throttled() & (1 >> 18))

def get_throttled_was_under_voltage():
    return bool(get_throttled() & (1 >> 16))
