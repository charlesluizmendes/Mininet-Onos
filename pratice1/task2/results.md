```
charles@charles-pc:~/Projetos/Mininet-Onos/pratice1/task2$ sudo ./run.sh single
Executando a topologia single
Tentando carregar o arquivo de configuração de: /home/charles/Projetos/Mininet-Onos/pratice1/task2/config.properties
Configurações carregadas: {'ip': '192.168.0.100', 'port': '6653'}
*** Criando topologia única com um switch e 13 hosts
*** Inicializando a rede com controlador remoto ONOS
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) (h4, s1) (h5, s1) (h6, s1) (h7, s1) (h8, s1) (h9, s1) (h10, s1) (h11, s1) (h12, s1) (h13, s1) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
*** Iniciando a rede
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Testando Conexão entre Hosts
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
h2 -> h1 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
h3 -> h1 h2 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
h4 -> h1 h2 h3 h5 h6 h7 h8 h9 h10 h11 h12 h13 
h5 -> h1 h2 h3 h4 h6 h7 h8 h9 h10 h11 h12 h13 
h6 -> h1 h2 h3 h4 h5 h7 h8 h9 h10 h11 h12 h13 
h7 -> h1 h2 h3 h4 h5 h6 h8 h9 h10 h11 h12 h13 
h8 -> h1 h2 h3 h4 h5 h6 h7 h9 h10 h11 h12 h13 
h9 -> h1 h2 h3 h4 h5 h6 h7 h8 h10 h11 h12 h13 
h10 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h11 h12 h13 
h11 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h12 h13 
h12 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h13 
h13 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 
*** Results: 0% dropped (156/156 received)
*** Parando a rede
*** Stopping 1 controllers
c0 
*** Stopping 13 links
.............
*** Stopping 1 switches
s1 
*** Stopping 13 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 
*** Done
```

```
charles@charles-pc:~/Projetos/Mininet-Onos/pratice1/task2$ sudo ./run.sh linear
Executando a topologia linear
Tentando carregar o arquivo de configuração de: /home/charles/Projetos/Mininet-Onos/pratice1/task2/config.properties
Configurações carregadas: {'ip': '192.168.0.100', 'port': '6653'}
*** Criando topologia linear com 10 switch(es) e 10 host(s)
*** Inicializando a rede com controlador remoto ONOS
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 
*** Adding links:
(h1, s1) (h2, s2) (h3, s3) (h4, s4) (h5, s5) (h6, s6) (h7, s7) (h8, s8) (h9, s9) (h10, s10) (s1, s2) (s2, s3) (s3, s4) (s4, s5) (s5, s6) (s6, s7) (s7, s8) (s8, s9) (s9, s10) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Iniciando a rede
*** Starting controller
c0 
*** Starting 10 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 ...
*** Testando Conexão entre Hosts
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 h8 h9 h10 
h2 -> h1 h3 h4 h5 h6 h7 h8 h9 h10 
h3 -> h1 h2 h4 h5 h6 h7 h8 h9 h10 
h4 -> h1 h2 h3 h5 h6 h7 h8 h9 h10 
h5 -> h1 h2 h3 h4 h6 h7 h8 h9 h10 
h6 -> h1 h2 h3 h4 h5 h7 h8 h9 h10 
h7 -> h1 h2 h3 h4 h5 h6 h8 h9 h10 
h8 -> h1 h2 h3 h4 h5 h6 h7 h9 h10 
h9 -> h1 h2 h3 h4 h5 h6 h7 h8 h10 
h10 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 
*** Results: 0% dropped (90/90 received)
*** Parando a rede
*** Stopping 1 controllers
c0 
*** Stopping 19 links
...................
*** Stopping 10 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 
*** Stopping 10 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Done
```

```
charles@charles-pc:~/Projetos/Mininet-Onos/pratice1/task2$ sudo ./run.sh tree
Executando a topologia tree
Tentando carregar o arquivo de configuração de: /home/charles/Projetos/Mininet-Onos/pratice1/task2/config.properties
Configurações carregadas: {'ip': '192.168.0.100', 'port': '6653'}
*** Criando topologia em árvore com depth 4 e fanout 5
*** Inicializando a rede com controlador remoto ONOS
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81 h82 h83 h84 h85 h86 h87 h88 h89 h90 h91 h92 h93 h94 h95 h96 h97 h98 h99 h100 h101 h102 h103 h104 h105 h106 h107 h108 h109 h110 h111 h112 h113 h114 h115 h116 h117 h118 h119 h120 h121 h122 h123 h124 h125 h126 h127 h128 h129 h130 h131 h132 h133 h134 h135 h136 h137 h138 h139 h140 h141 h142 h143 h144 h145 h146 h147 h148 h149 h150 h151 h152 h153 h154 h155 h156 h157 h158 h159 h160 h161 h162 h163 h164 h165 h166 h167 h168 h169 h170 h171 h172 h173 h174 h175 h176 h177 h178 h179 h180 h181 h182 h183 h184 h185 h186 h187 h188 h189 h190 h191 h192 h193 h194 h195 h196 h197 h198 h199 h200 h201 h202 h203 h204 h205 h206 h207 h208 h209 h210 h211 h212 h213 h214 h215 h216 h217 h218 h219 h220 h221 h222 h223 h224 h225 h226 h227 h228 h229 h230 h231 h232 h233 h234 h235 h236 h237 h238 h239 h240 h241 h242 h243 h244 h245 h246 h247 h248 h249 h250 h251 h252 h253 h254 h255 h256 h257 h258 h259 h260 h261 h262 h263 h264 h265 h266 h267 h268 h269 h270 h271 h272 h273 h274 h275 h276 h277 h278 h279 h280 h281 h282 h283 h284 h285 h286 h287 h288 h289 h290 h291 h292 h293 h294 h295 h296 h297 h298 h299 h300 h301 h302 h303 h304 h305 h306 h307 h308 h309 h310 h311 h312 h313 h314 h315 h316 h317 h318 h319 h320 h321 h322 h323 h324 h325 h326 h327 h328 h329 h330 h331 h332 h333 h334 h335 h336 h337 h338 h339 h340 h341 h342 h343 h344 h345 h346 h347 h348 h349 h350 h351 h352 h353 h354 h355 h356 h357 h358 h359 h360 h361 h362 h363 h364 h365 h366 h367 h368 h369 h370 h371 h372 h373 h374 h375 h376 h377 h378 h379 h380 h381 h382 h383 h384 h385 h386 h387 h388 h389 h390 h391 h392 h393 h394 h395 h396 h397 h398 h399 h400 h401 h402 h403 h404 h405 h406 h407 h408 h409 h410 h411 h412 h413 h414 h415 h416 h417 h418 h419 h420 h421 h422 h423 h424 h425 h426 h427 h428 h429 h430 h431 h432 h433 h434 h435 h436 h437 h438 h439 h440 h441 h442 h443 h444 h445 h446 h447 h448 h449 h450 h451 h452 h453 h454 h455 h456 h457 h458 h459 h460 h461 h462 h463 h464 h465 h466 h467 h468 h469 h470 h471 h472 h473 h474 h475 h476 h477 h478 h479 h480 h481 h482 h483 h484 h485 h486 h487 h488 h489 h490 h491 h492 h493 h494 h495 h496 h497 h498 h499 h500 h501 h502 h503 h504 h505 h506 h507 h508 h509 h510 h511 h512 h513 h514 h515 h516 h517 h518 h519 h520 h521 h522 h523 h524 h525 h526 h527 h528 h529 h530 h531 h532 h533 h534 h535 h536 h537 h538 h539 h540 h541 h542 h543 h544 h545 h546 h547 h548 h549 h550 h551 h552 h553 h554 h555 h556 h557 h558 h559 h560 h561 h562 h563 h564 h565 h566 h567 h568 h569 h570 h571 h572 h573 h574 h575 h576 h577 h578 h579 h580 h581 h582 h583 h584 h585 h586 h587 h588 h589 h590 h591 h592 h593 h594 h595 h596 h597 h598 h599 h600 h601 h602 h603 h604 h605 h606 h607 h608 h609 h610 h611 h612 h613 h614 h615 h616 h617 h618 h619 h620 h621 h622 h623 h624 h625 
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 s41 s42 s43 s44 s45 s46 s47 s48 s49 s50 s51 s52 s53 s54 s55 s56 s57 s58 s59 s60 s61 s62 s63 s64 s65 s66 s67 s68 s69 s70 s71 s72 s73 s74 s75 s76 s77 s78 s79 s80 s81 s82 s83 s84 s85 s86 s87 s88 s89 s90 s91 s92 s93 s94 s95 s96 s97 s98 s99 s100 s101 s102 s103 s104 s105 s106 s107 s108 s109 s110 s111 s112 s113 s114 s115 s116 s117 s118 s119 s120 s121 s122 s123 s124 s125 s126 s127 s128 s129 s130 s131 s132 s133 s134 s135 s136 s137 s138 s139 s140 s141 s142 s143 s144 s145 s146 s147 s148 s149 s150 s151 s152 s153 s154 s155 s156 
*** Adding links:
(s1, s2) (s1, s33) (s1, s64) (s1, s95) (s1, s126) (s2, s3) (s2, s9) (s2, s15) (s2, s21) (s2, s27) (s3, s4) (s3, s5) (s3, s6) (s3, s7) (s3, s8) (s4, h1) (s4, h2) (s4, h3) (s4, h4) (s4, h5) (s5, h6) (s5, h7) (s5, h8) (s5, h9) (s5, h10) (s6, h11) (s6, h12) (s6, h13) (s6, h14) (s6, h15) (s7, h16) (s7, h17) (s7, h18) (s7, h19) (s7, h20) (s8, h21) (s8, h22) (s8, h23) (s8, h24) (s8, h25) (s9, s10) (s9, s11) (s9, s12) (s9, s13) (s9, s14) (s10, h26) (s10, h27) (s10, h28) (s10, h29) (s10, h30) (s11, h31) (s11, h32) (s11, h33) (s11, h34) (s11, h35) (s12, h36) (s12, h37) (s12, h38) (s12, h39) (s12, h40) (s13, h41) (s13, h42) (s13, h43) (s13, h44) (s13, h45) (s14, h46) (s14, h47) (s14, h48) (s14, h49) (s14, h50) (s15, s16) (s15, s17) (s15, s18) (s15, s19) (s15, s20) (s16, h51) (s16, h52) (s16, h53) (s16, h54) (s16, h55) (s17, h56) (s17, h57) (s17, h58) (s17, h59) (s17, h60) (s18, h61) (s18, h62) (s18, h63) (s18, h64) (s18, h65) (s19, h66) (s19, h67) (s19, h68) (s19, h69) (s19, h70) (s20, h71) (s20, h72) (s20, h73) (s20, h74) (s20, h75) (s21, s22) (s21, s23) (s21, s24) (s21, s25) (s21, s26) (s22, h76) (s22, h77) (s22, h78) (s22, h79) (s22, h80) (s23, h81) (s23, h82) (s23, h83) (s23, h84) (s23, h85) (s24, h86) (s24, h87) (s24, h88) (s24, h89) (s24, h90) (s25, h91) (s25, h92) (s25, h93) (s25, h94) (s25, h95) (s26, h96) (s26, h97) (s26, h98) (s26, h99) (s26, h100) (s27, s28) (s27, s29) (s27, s30) (s27, s31) (s27, s32) (s28, h101) (s28, h102) (s28, h103) (s28, h104) (s28, h105) (s29, h106) (s29, h107) (s29, h108) (s29, h109) (s29, h110) (s30, h111) (s30, h112) (s30, h113) (s30, h114) (s30, h115) (s31, h116) (s31, h117) (s31, h118) (s31, h119) (s31, h120) (s32, h121) (s32, h122) (s32, h123) (s32, h124) (s32, h125) (s33, s34) (s33, s40) (s33, s46) (s33, s52) (s33, s58) (s34, s35) (s34, s36) (s34, s37) (s34, s38) (s34, s39) (s35, h126) (s35, h127) (s35, h128) (s35, h129) (s35, h130) (s36, h131) (s36, h132) (s36, h133) (s36, h134) (s36, h135) (s37, h136) (s37, h137) (s37, h138) (s37, h139) (s37, h140) (s38, h141) (s38, h142) (s38, h143) (s38, h144) (s38, h145) (s39, h146) (s39, h147) (s39, h148) (s39, h149) (s39, h150) (s40, s41) (s40, s42) (s40, s43) (s40, s44) (s40, s45) (s41, h151) (s41, h152) (s41, h153) (s41, h154) (s41, h155) (s42, h156) (s42, h157) (s42, h158) (s42, h159) (s42, h160) (s43, h161) (s43, h162) (s43, h163) (s43, h164) (s43, h165) (s44, h166) (s44, h167) (s44, h168) (s44, h169) (s44, h170) (s45, h171) (s45, h172) (s45, h173) (s45, h174) (s45, h175) (s46, s47) (s46, s48) (s46, s49) (s46, s50) (s46, s51) (s47, h176) (s47, h177) (s47, h178) (s47, h179) (s47, h180) (s48, h181) (s48, h182) (s48, h183) (s48, h184) (s48, h185) (s49, h186) (s49, h187) (s49, h188) (s49, h189) (s49, h190) (s50, h191) (s50, h192) (s50, h193) (s50, h194) (s50, h195) (s51, h196) (s51, h197) (s51, h198) (s51, h199) (s51, h200) (s52, s53) (s52, s54) (s52, s55) (s52, s56) (s52, s57) (s53, h201) (s53, h202) (s53, h203) (s53, h204) (s53, h205) (s54, h206) (s54, h207) (s54, h208) (s54, h209) (s54, h210) (s55, h211) (s55, h212) (s55, h213) (s55, h214) (s55, h215) (s56, h216) (s56, h217) (s56, h218) (s56, h219) (s56, h220) (s57, h221) (s57, h222) (s57, h223) (s57, h224) (s57, h225) (s58, s59) (s58, s60) (s58, s61) (s58, s62) (s58, s63) (s59, h226) (s59, h227) (s59, h228) (s59, h229) (s59, h230) (s60, h231) (s60, h232) (s60, h233) (s60, h234) (s60, h235) (s61, h236) (s61, h237) (s61, h238) (s61, h239) (s61, h240) (s62, h241) (s62, h242) (s62, h243) (s62, h244) (s62, h245) (s63, h246) (s63, h247) (s63, h248) (s63, h249) (s63, h250) (s64, s65) (s64, s71) (s64, s77) (s64, s83) (s64, s89) (s65, s66) (s65, s67) (s65, s68) (s65, s69) (s65, s70) (s66, h251) (s66, h252) (s66, h253) (s66, h254) (s66, h255) (s67, h256) (s67, h257) (s67, h258) (s67, h259) (s67, h260) (s68, h261) (s68, h262) (s68, h263) (s68, h264) (s68, h265) (s69, h266) (s69, h267) (s69, h268) (s69, h269) (s69, h270) (s70, h271) (s70, h272) (s70, h273) (s70, h274) (s70, h275) (s71, s72) (s71, s73) (s71, s74) (s71, s75) (s71, s76) (s72, h276) (s72, h277) (s72, h278) (s72, h279) (s72, h280) (s73, h281) (s73, h282) (s73, h283) (s73, h284) (s73, h285) (s74, h286) (s74, h287) (s74, h288) (s74, h289) (s74, h290) (s75, h291) (s75, h292) (s75, h293) (s75, h294) (s75, h295) (s76, h296) (s76, h297) (s76, h298) (s76, h299) (s76, h300) (s77, s78) (s77, s79) (s77, s80) (s77, s81) (s77, s82) (s78, h301) (s78, h302) (s78, h303) (s78, h304) (s78, h305) (s79, h306) (s79, h307) (s79, h308) (s79, h309) (s79, h310) (s80, h311) (s80, h312) (s80, h313) (s80, h314) (s80, h315) (s81, h316) (s81, h317) (s81, h318) (s81, h319) (s81, h320) (s82, h321) (s82, h322) (s82, h323) (s82, h324) (s82, h325) (s83, s84) (s83, s85) (s83, s86) (s83, s87) (s83, s88) (s84, h326) (s84, h327) (s84, h328) (s84, h329) (s84, h330) (s85, h331) (s85, h332) (s85, h333) (s85, h334) (s85, h335) (s86, h336) (s86, h337) (s86, h338) (s86, h339) (s86, h340) (s87, h341) (s87, h342) (s87, h343) (s87, h344) (s87, h345) (s88, h346) (s88, h347) (s88, h348) (s88, h349) (s88, h350) (s89, s90) (s89, s91) (s89, s92) (s89, s93) (s89, s94) (s90, h351) (s90, h352) (s90, h353) (s90, h354) (s90, h355) (s91, h356) (s91, h357) (s91, h358) (s91, h359) (s91, h360) (s92, h361) (s92, h362) (s92, h363) (s92, h364) (s92, h365) (s93, h366) (s93, h367) (s93, h368) (s93, h369) (s93, h370) (s94, h371) (s94, h372) (s94, h373) (s94, h374) (s94, h375) (s95, s96) (s95, s102) (s95, s108) (s95, s114) (s95, s120) (s96, s97) (s96, s98) (s96, s99) (s96, s100) (s96, s101) (s97, h376) (s97, h377) (s97, h378) (s97, h379) (s97, h380) (s98, h381) (s98, h382) (s98, h383) (s98, h384) (s98, h385) (s99, h386) (s99, h387) (s99, h388) (s99, h389) (s99, h390) (s100, h391) (s100, h392) (s100, h393) (s100, h394) (s100, h395) (s101, h396) (s101, h397) (s101, h398) (s101, h399) (s101, h400) (s102, s103) (s102, s104) (s102, s105) (s102, s106) (s102, s107) (s103, h401) (s103, h402) (s103, h403) (s103, h404) (s103, h405) (s104, h406) (s104, h407) (s104, h408) (s104, h409) (s104, h410) (s105, h411) (s105, h412) (s105, h413) (s105, h414) (s105, h415) (s106, h416) (s106, h417) (s106, h418) (s106, h419) (s106, h420) (s107, h421) (s107, h422) (s107, h423) (s107, h424) (s107, h425) (s108, s109) (s108, s110) (s108, s111) (s108, s112) (s108, s113) (s109, h426) (s109, h427) (s109, h428) (s109, h429) (s109, h430) (s110, h431) (s110, h432) (s110, h433) (s110, h434) (s110, h435) (s111, h436) (s111, h437) (s111, h438) (s111, h439) (s111, h440) (s112, h441) (s112, h442) (s112, h443) (s112, h444) (s112, h445) (s113, h446) (s113, h447) (s113, h448) (s113, h449) (s113, h450) (s114, s115) (s114, s116) (s114, s117) (s114, s118) (s114, s119) (s115, h451) (s115, h452) (s115, h453) (s115, h454) (s115, h455) (s116, h456) (s116, h457) (s116, h458) (s116, h459) (s116, h460) (s117, h461) (s117, h462) (s117, h463) (s117, h464) (s117, h465) (s118, h466) (s118, h467) (s118, h468) (s118, h469) (s118, h470) (s119, h471) (s119, h472) (s119, h473) (s119, h474) (s119, h475) (s120, s121) (s120, s122) (s120, s123) (s120, s124) (s120, s125) (s121, h476) (s121, h477) (s121, h478) (s121, h479) (s121, h480) (s122, h481) (s122, h482) (s122, h483) (s122, h484) (s122, h485) (s123, h486) (s123, h487) (s123, h488) (s123, h489) (s123, h490) (s124, h491) (s124, h492) (s124, h493) (s124, h494) (s124, h495) (s125, h496) (s125, h497) (s125, h498) (s125, h499) (s125, h500) (s126, s127) (s126, s133) (s126, s139) (s126, s145) (s126, s151) (s127, s128) (s127, s129) (s127, s130) (s127, s131) (s127, s132) (s128, h501) (s128, h502) (s128, h503) (s128, h504) (s128, h505) (s129, h506) (s129, h507) (s129, h508) (s129, h509) (s129, h510) (s130, h511) (s130, h512) (s130, h513) (s130, h514) (s130, h515) (s131, h516) (s131, h517) (s131, h518) (s131, h519) (s131, h520) (s132, h521) (s132, h522) (s132, h523) (s132, h524) (s132, h525) (s133, s134) (s133, s135) (s133, s136) (s133, s137) (s133, s138) (s134, h526) (s134, h527) (s134, h528) (s134, h529) (s134, h530) (s135, h531) (s135, h532) (s135, h533) (s135, h534) (s135, h535) (s136, h536) (s136, h537) (s136, h538) (s136, h539) (s136, h540) (s137, h541) (s137, h542) (s137, h543) (s137, h544) (s137, h545) (s138, h546) (s138, h547) (s138, h548) (s138, h549) (s138, h550) (s139, s140) (s139, s141) (s139, s142) (s139, s143) (s139, s144) (s140, h551) (s140, h552) (s140, h553) (s140, h554) (s140, h555) (s141, h556) (s141, h557) (s141, h558) (s141, h559) (s141, h560) (s142, h561) (s142, h562) (s142, h563) (s142, h564) (s142, h565) (s143, h566) (s143, h567) (s143, h568) (s143, h569) (s143, h570) (s144, h571) (s144, h572) (s144, h573) (s144, h574) (s144, h575) (s145, s146) (s145, s147) (s145, s148) (s145, s149) (s145, s150) (s146, h576) (s146, h577) (s146, h578) (s146, h579) (s146, h580) (s147, h581) (s147, h582) (s147, h583) (s147, h584) (s147, h585) (s148, h586) (s148, h587) (s148, h588) (s148, h589) (s148, h590) (s149, h591) (s149, h592) (s149, h593) (s149, h594) (s149, h595) (s150, h596) (s150, h597) (s150, h598) (s150, h599) (s150, h600) (s151, s152) (s151, s153) (s151, s154) (s151, s155) (s151, s156) (s152, h601) (s152, h602) (s152, h603) (s152, h604) (s152, h605) (s153, h606) (s153, h607) (s153, h608) (s153, h609) (s153, h610) (s154, h611) (s154, h612) (s154, h613) (s154, h614) (s154, h615) (s155, h616) (s155, h617) (s155, h618) (s155, h619) (s155, h620) (s156, h621) (s156, h622) (s156, h623) (s156, h624) (s156, h625) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81 h82 h83 h84 h85 h86 h87 h88 h89 h90 h91 h92 h93 h94 h95 h96 h97 h98 h99 h100 h101 h102 h103 h104 h105 h106 h107 h108 h109 h110 h111 h112 h113 h114 h115 h116 h117 h118 h119 h120 h121 h122 h123 h124 h125 h126 h127 h128 h129 h130 h131 h132 h133 h134 h135 h136 h137 h138 h139 h140 h141 h142 h143 h144 h145 h146 h147 h148 h149 h150 h151 h152 h153 h154 h155 h156 h157 h158 h159 h160 h161 h162 h163 h164 h165 h166 h167 h168 h169 h170 h171 h172 h173 h174 h175 h176 h177 h178 h179 h180 h181 h182 h183 h184 h185 h186 h187 h188 h189 h190 h191 h192 h193 h194 h195 h196 h197 h198 h199 h200 h201 h202 h203 h204 h205 h206 h207 h208 h209 h210 h211 h212 h213 h214 h215 h216 h217 h218 h219 h220 h221 h222 h223 h224 h225 h226 h227 h228 h229 h230 h231 h232 h233 h234 h235 h236 h237 h238 h239 h240 h241 h242 h243 h244 h245 h246 h247 h248 h249 h250 h251 h252 h253 h254 h255 h256 h257 h258 h259 h260 h261 h262 h263 h264 h265 h266 h267 h268 h269 h270 h271 h272 h273 h274 h275 h276 h277 h278 h279 h280 h281 h282 h283 h284 h285 h286 h287 h288 h289 h290 h291 h292 h293 h294 h295 h296 h297 h298 h299 h300 h301 h302 h303 h304 h305 h306 h307 h308 h309 h310 h311 h312 h313 h314 h315 h316 h317 h318 h319 h320 h321 h322 h323 h324 h325 h326 h327 h328 h329 h330 h331 h332 h333 h334 h335 h336 h337 h338 h339 h340 h341 h342 h343 h344 h345 h346 h347 h348 h349 h350 h351 h352 h353 h354 h355 h356 h357 h358 h359 h360 h361 h362 h363 h364 h365 h366 h367 h368 h369 h370 h371 h372 h373 h374 h375 h376 h377 h378 h379 h380 h381 h382 h383 h384 h385 h386 h387 h388 h389 h390 h391 h392 h393 h394 h395 h396 h397 h398 h399 h400 h401 h402 h403 h404 h405 h406 h407 h408 h409 h410 h411 h412 h413 h414 h415 h416 h417 h418 h419 h420 h421 h422 h423 h424 h425 h426 h427 h428 h429 h430 h431 h432 h433 h434 h435 h436 h437 h438 h439 h440 h441 h442 h443 h444 h445 h446 h447 h448 h449 h450 h451 h452 h453 h454 h455 h456 h457 h458 h459 h460 h461 h462 h463 h464 h465 h466 h467 h468 h469 h470 h471 h472 h473 h474 h475 h476 h477 h478 h479 h480 h481 h482 h483 h484 h485 h486 h487 h488 h489 h490 h491 h492 h493 h494 h495 h496 h497 h498 h499 h500 h501 h502 h503 h504 h505 h506 h507 h508 h509 h510 h511 h512 h513 h514 h515 h516 h517 h518 h519 h520 h521 h522 h523 h524 h525 h526 h527 h528 h529 h530 h531 h532 h533 h534 h535 h536 h537 h538 h539 h540 h541 h542 h543 h544 h545 h546 h547 h548 h549 h550 h551 h552 h553 h554 h555 h556 h557 h558 h559 h560 h561 h562 h563 h564 h565 h566 h567 h568 h569 h570 h571 h572 h573 h574 h575 h576 h577 h578 h579 h580 h581 h582 h583 h584 h585 h586 h587 h588 h589 h590 h591 h592 h593 h594 h595 h596 h597 h598 h599 h600 h601 h602 h603 h604 h605 h606 h607 h608 h609 h610 h611 h612 h613 h614 h615 h616 h617 h618 h619 h620 h621 h622 h623 h624 h625 
*** Iniciando a rede
*** Starting controller
c0 
*** Starting 156 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 s41 s42 s43 s44 s45 s46 s47 s48 s49 s50 s51 s52 s53 s54 s55 s56 s57 s58 s59 s60 s61 s62 s63 s64 s65 s66 s67 s68 s69 s70 s71 s72 s73 s74 s75 s76 s77 s78 s79 s80 s81 s82 s83 s84 s85 s86 s87 s88 s89 s90 s91 s92 s93 s94 s95 s96 s97 s98 s99 s100 s101 s102 s103 s104 s105 s106 s107 s108 s109 s110 s111 s112 s113 s114 s115 s116 s117 s118 s119 s120 s121 s122 s123 s124 s125 s126 s127 s128 s129 s130 s131 s132 s133 s134 s135 s136 s137 s138 s139 s140 s141 s142 s143 s144 s145 s146 s147 s148 s149 s150 s151 s152 s153 s154 s155 s156 ...
```