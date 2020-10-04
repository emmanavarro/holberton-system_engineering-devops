# 0x19. Postmortem

## Incident #1 - Error 503 caused by environmental emergency

## Author: Emma Navarro 

## Status: Closed

## Summary of issues established during the emergency

Initially, the service provided by our server was inactive for 2 hours on October 3, 2020, between 5 pm and 7 pm Pacific time. During this time, a large number of requests made by users were denied and responded with an error 503 referring to service unavailable. During this lapse, the DevOps junior engineer tried to restore the server service by applying different configurations to try to achieve its correct operation, and in this setting, he found out that several power lines and wiring got damaged along the company perimeters due to a strong thunderstorm that occurred at the same hours in the afternoon. The company in charge of solving these issues was immediately requested to be present on-site to solve it.

## Schedule or Timeline

| Time | Date | Action |
|------|------|--------|
| 5:00 pm | 05/22/2020 | The service provided by our server goes down. |
| 5:25 pm | 05/22/2020 | Automatic server restart. |
| 5:40 pm | 05/22/2020 | Manual reset and manual configuration. |
| 6:00 pm | 05/22/2020 | Third-party intervention is requested. |
| 6:10 pm | 05/22/2020 | Call the service in charge of providing us wiring. |
| 6:35 pm | 05/22/2020 | The company in charge replaced and connected the new wiring. |

## Root cause

In the afternoon there was a strong thunderstorm accompanied by heavy rains which caused great problems in the area, not only in the city's public wiring but also in the private infrastructure of different companies in this area. During the first 20 minutes at the beginning of the storm, at approximately 4:45 pm on October 3 of 2020, the staff believed that the situation was only about an electric power failure and it would be solved with the company's power generating plant running and, after 25 minutes the server was restarted automatically. But the server did not return an active state (OK) so this process ended. Then, The engineer checked to see if it was a local problem but several attempts to restart and manual configuration did not give results. At that time the engineer asked third-parties if any news had been reported outside the company to know if that affected it, they answered back saying that there was damage in the surroundings of the company and at that moment the engineer realized that the cause was completely unrelated to the possibilities to restore the service internally.

## Resolution and Recovery

Once the cause was determined as external, the corresponding reports were made to the external company in charge of solving these technical problems. Regarding its physical infrastructure, after 25 minutes from the initial report until the arrival of the external company providing the wiring service, it was possible to reestablish the operation of the server.

## Corrective and preventive measures

A prevention scheme was conducted to determine that a system of wired connections to the exterior should be setted belowground to avoid this type of problem when an environmental disaster occurs again.
