/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */
CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
//	config.language = 'fr';
//	config.uiColor = '#AADC6E';
//	config.language = 'en';
    config.enterMode = CKEDITOR.ENTER_BR; //remove 'p' tag after enter
    config.shiftEnterMode = CKEDITOR.ENTER_P; //add 'p' tag after shift+enter
};