
project(winrtutils)

generate_product_version(
   versioninfo
   NAME "LunaTranslator winrtutils"
   COMPANY_COPYRIGHT "HIllya51 (C) 2024"
   VERSION_MAJOR ${VERSION_MAJOR}
   VERSION_MINOR ${VERSION_MINOR}
   VERSION_PATCH ${VERSION_PATCH}
)

add_library(winrtutils MODULE winrtsnapshot.cpp winrtocr.cpp livecaptions.cpp ${versioninfo})
target_precompile_headers(winrtutils REUSE_FROM pch) 
target_link_libraries(winrtutils wil dwmapi)
if(${CMAKE_SIZEOF_VOID_P} EQUAL 8)
	set_target_properties(winrtutils PROPERTIES OUTPUT_NAME "winrtutils64")
else()
	set_target_properties(winrtutils PROPERTIES OUTPUT_NAME "winrtutils32")
endif()

